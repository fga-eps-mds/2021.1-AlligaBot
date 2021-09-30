# -*- coding: utf-8 -*-

import os
from os import path

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

import pandas as pd
import requests
import patoolib

class DadosDoCovidPeloCsvAction(Action):

    def __init__(self):
        self.diretorio = 'covid_data'
        self.arquivo = 'dados_covid_csv.gz'
        self.url = 'https://data.brasil.io/dataset/covid19/caso.csv.gz'
        caminho_arquivo = ''

        if self.arquivo_baixado_ha_mais_de_um_dia(caminho_arquivo):
            self.resposta = requests.get(self.url)

            if self.resposta.status_code == requests.codes.OK:
                caminho_arquivo = path.join(self.diretorio, self.arquivo)
                with open(caminho_arquivo, 'wb') as novo_arquivo:
                    novo_arquivo.write(self.resposta.content)
                    print(f'Download finalizado. Arquivo salvo em: {caminho_arquivo}')
            else:
                self.resposta.raise_for_status()

            patoolib.extract_archive(caminho_arquivo, outdir=self.diretorio)

    def name(self) -> Text:
        return 'action_dados_covid_baseados_em_localizacao'
    
    def arquivo_baixado_ha_mais_de_um_dia(self, caminho_do_arquivo: str):
        # os.stat(caminho_do_arquivo).
        return True

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        uf = tracker.get_slot('uf')
        cidade = tracker.get_slot('cidade')

        self.dados = pd.read_csv(
            path.join(self.diretorio, 'caso.csv'),
            sep = ',',
            decimal = '.'
        )

        dataframe = pd.DataFrame(self.dados)

        pesquisa_por_uf = dataframe.loc[dataframe['state'] == uf]
        pesquisa_por_ultimo_dado = pesquisa_por_uf.loc[dataframe['is_last'] == True]
        pesquisa_por_cidade = pesquisa_por_ultimo_dado.loc[dataframe['city'] == cidade]

        pesquisa_por_cidade = pesquisa_por_cidade[
            [
                'date',
                'state', 
                'city', 
                'estimated_population_2019',
                'confirmed',
                'deaths',
                'confirmed_per_100k_inhabitants',
            ]
        ]

        conteudo = ''
        for label, content in pesquisa_por_cidade.items():
            conteudo += label + ': ' + str(content.to_list()[0]) + '\n'

        dispatcher.utter_message(text=conteudo)
        
        return [AllSlotsReset()]
