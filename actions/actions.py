# -*- coding: utf-8 -*-

import os
import time
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
        self.diretorio = path.join(path.dirname(path.realpath(__file__)), 'covid_data')
        self.arquivo = 'dados_covid_csv.gz'
        self.url = 'https://data.brasil.io/dataset/covid19/caso.csv.gz'
        self.TEMPO_LIMITE_PARA_ATUALIZACAO_EM_DIAS = 1
        self.caminho_arquivo = path.join(self.diretorio, self.arquivo)


    def name(self) -> Text:
        return 'action_dados_covid_baseados_em_localizacao'
            

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        print('antes do if')
        
        arquivo_csv_existe = self.arquivo_csv_existe()
        if not arquivo_csv_existe or (arquivo_csv_existe and self.arquivo_csv_baixado_ha_mais_de_um_dia()):
            self.baixar_e_extrair_arquivo_csv()

        uf = tracker.get_slot('uf')
        cidade = tracker.get_slot('cidade')

        self.dados = pd.read_csv(
            path.join(self.diretorio, 'dados_covid_csv'),
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
    

    def arquivo_csv_existe(self) -> bool:
        return path.isfile(self.caminho_arquivo)
    

    def arquivo_csv_baixado_ha_mais_de_um_dia(self) -> bool:
        SEGUNDOS_PARA_DIAS = 60 * 60 * 24
        instante_atual = time.time()
        instante_da_ultima_modificacao_arquivo = os.stat(self.caminho_arquivo).st_mtime

        print(instante_da_ultima_modificacao_arquivo)

        diferenca_de_instante_em_seg = instante_atual - instante_da_ultima_modificacao_arquivo
        print('Diferenca de tempo em segundos', diferenca_de_instante_em_seg)
        print('Diferenca de dias em segundos', diferenca_de_instante_em_seg / SEGUNDOS_PARA_DIAS)

        return (diferenca_de_instante_em_seg / SEGUNDOS_PARA_DIAS) > self.TEMPO_LIMITE_PARA_ATUALIZACAO_EM_DIAS

    
    def baixar_e_extrair_arquivo_csv(self) -> None:
        print('baixando arquivo atualizado')
        self.resposta = requests.get(self.url)

        if self.resposta.status_code == requests.codes.OK:
            with open(self.caminho_arquivo, 'wb') as novo_arquivo:
                novo_arquivo.write(self.resposta.content)
                print(f'Download finalizado. Arquivo salvo em: {self.caminho_arquivo}')
        else:
            self.resposta.raise_for_status()

        patoolib.extract_archive(self.caminho_arquivo, outdir=self.diretorio)
        return
