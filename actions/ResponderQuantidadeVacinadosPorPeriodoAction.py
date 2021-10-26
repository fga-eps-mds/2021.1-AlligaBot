# -*- coding: utf-8 -*-

import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from os import path
from typing import Any, Text, Dict, List


class ResponderQuantidadeVacinadosPorPeriodoAction(Action):
    def __init__(self) -> None:
        self.url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'

        
        return
    
    def name(self) -> Text:
        return 'action_responder_quantidade_vacinados_por_periodo'
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        # zfill(qtd_zeros_a_esquerda) - Garante que sempre terá x zeros a esquerda

        dia = f'{tracker.get_slot("dia")}'.zfill(2)
        mes = f'{tracker.get_slot("mes")}'.zfill(2)
        ano = tracker.get_slot('ano')

        data_informada = f'{ano}-{mes}-{dia}'

        dados = pd.read_csv(
            self.url,
            sep = ',',
            decimal = '.'
        )

        dataframe = pd.DataFrame(dados)

        dataframe_data = dataframe.loc[dataframe['date'] == data_informada]
        if dataframe_data.empty:
            mensagem_erro = f'Não consegui encontrar nenhum registro para a data {data_informada} 🥺. Lembre-se de informar valores válidos e somente o número do dia, do mês e do ano 😉'
            dispatcher.utter_message(text=mensagem_erro)
           
            return [AllSlotsReset()]

        data_br = f'{dia}/{mes}/{ano}'

        # Realiza a soma de todos os casos de vacinados naquele dia em todas as cidades
        total_vacinados_por_periodo_no_brasil = dataframe_data['vaccinated'].sum()

        mensagem = 'Essas são as informações que consegui encontrar 🕵️‍♂️\n\n'
        mensagem += f'O total de vacinados no Brasil no período de {data_br} foi de {total_vacinados_por_periodo_no_brasil:,.2f} pessoas'
        mensagem += '\n\nEspero ter ajudado com estas informações 😊'
        
        dispatcher.utter_message(text=mensagem)
        
        return [AllSlotsReset()]