# -*- coding: utf-8 -*-
from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

from genericpath import isdir
import shutil
import pandas as pd
from pandas.core.tools import numeric
import numpy as np
import requests
import patoolib

from io import BytesIO
import os


class JokeAction(Action):
    def name(self) -> Text:
        return "action_joke"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        req = requests.get(
            'https://official-joke-api.appspot.com/jokes/random').json()
        setup = req['setup']

        punchline = req['punchline']
        dispatcher.utter_message(text=setup)
        dispatcher.utter_message(text=punchline)
        print("hello")
        return []

class DadosDoCovidPeloCsvAction(Action):

    def __init__(self):
        self.diretorio = './covid_data'
        self.arquivo = 'dados_covid_csv.zip'

        if not os.path.isdir(self.diretorio):
            os.makedirs(self.diretorio)

            self.url = 'https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/32fc907e8d6ee3a669d31af4a16deb26_HIST_PAINEL_COVIDBR_19set2021.zip'

            self.resposta = requests.get(self.url)

            if self.resposta.status_code == requests.codes.OK:
                with open(self.diretorio + '/' + self.arquivo, 'wb') as novo_arquivo:
                    novo_arquivo.write(self.resposta.content)
                    print("Download finalizado. Arquivo salvo em: {}".format(self.diretorio + '/' + self.arquivo))
            else:
                self.resposta.raise_for_status()

            patoolib.extract_archive(self.diretorio + '/' + self.arquivo, outdir=self.diretorio)

    def name(self) -> Text:
        return "action_dados_covid_baseados_em_localizacao"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        uf = tracker.get_slot('uf')
        cidade = tracker.get_slot('cidade')

        self.dados = pd.read_csv(
            self.diretorio + '/HIST_PAINEL_COVIDBR_2021_Parte2_19set2021.csv',
            sep = ';',
            decimal = '.'
        )

        dataframe = pd.DataFrame(self.dados)

        pesquisa_por_uf = dataframe.loc[dataframe['estado'] == uf]
        pesquisa_por_data = pesquisa_por_uf.loc[dataframe['data'] == '2021-09-18']
        pesquisa_por_cidade = pesquisa_por_data.loc[dataframe['municipio'] == cidade]

        conteudo = ''

        for label, content in pesquisa_por_cidade.items():
            conteudo += label + ': ' + str(content.to_list()[0]) + '\n'

        dispatcher.utter_message(text=conteudo)
        
        return [AllSlotsReset()]
