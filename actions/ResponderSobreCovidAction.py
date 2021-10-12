# -*- coding: utf-8 -*-

import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from os import path
from datetime import datetime
from typing import Any, Text, Dict, List

class ResponderSobreCovidAction(Action):
    def __init__(self) -> None:
        self.url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv'
        return
    
    def name(self) -> Text:
        return 'action_dados_covid_baseados_em_localizacao'
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        uf = tracker.get_slot('uf').upper()
        cidade = tracker.get_slot('cidade').capitalize()
        cidade = f'{cidade}/{uf}'

        dados = pd.read_csv(
            self.url,
            sep = ',',
            decimal = '.'
        )

        dataframe = pd.DataFrame(dados)

        dataframe_estado = dataframe.loc[dataframe['state'] == uf]
        if dataframe_estado.empty:
            mensagem_erro = f'Não consegui encontrar o estado {uf} 🥺. Lembre-se de informar somente a sigla, exemplo: DF 😉'
            dispatcher.utter_message(text=mensagem_erro)
            return [AllSlotsReset()]

        dataframe_cidade = dataframe_estado.loc[dataframe_estado['city'] == cidade]
        if dataframe_cidade.empty:
            mensagem_erro = f'Não achei a cidade {cidade} 🥺. Por favor, escreva o nome da cidade respeitando os acentos e sem abreviações 😉'
            dispatcher.utter_message(text=mensagem_erro)
            return [AllSlotsReset()]

        dataframe_cidade = dataframe_cidade[
            [
                'last_info_date', 
                'state', 
                'city', 
                'deaths', 
                'totalCases', 
                'deaths_per_100k_inhabitants', 
                'totalCases_per_100k_inhabitants',
            ]
        ]

        ingles_para_portugues = {
            'last_info_date': 'Data',
            'state': 'Estado', 
            'city': 'Cidade', 
            'deaths': 'Mortes',
            'totalCases': 'Total de casos',
            'deaths_per_100k_inhabitants': 'Total de mortes por 100 mil habitantes',
            'totalCases_per_100k_inhabitants': 'Total de casos por 100 mil habitantes',
        }

        mensagem = 'Estas são as informações que consegui encontrar 🕵️‍♂️\n\n'
        
        for rotulo_ingles, content in dataframe_cidade.items():
            rotulo_portugues = ingles_para_portugues[rotulo_ingles]

            if rotulo_portugues == 'Data':
                data = datetime.strptime(str(content.to_list()[0]), '%Y-%m-%d')
                data = f'{data.day}/{data.month}/{data.year}'

                mensagem += f'{rotulo_portugues}: {data}\n'
            else:
                mensagem += f'{rotulo_portugues}: {str(content.to_list()[0])}\n'

        mensagem += '\nEspero ter ajudado com estas informações 😊'
        
        dispatcher.utter_message(text=mensagem)
        
        return [AllSlotsReset()]
