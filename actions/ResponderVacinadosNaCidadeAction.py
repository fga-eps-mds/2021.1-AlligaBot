# -*- coding: utf-8 -*-

import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from os import path
from typing import Any, Text, Dict, List

diretorio = path.join(path.dirname(path.realpath(__file__)), 'covid_data')

class ResponderVacinadosNaCidadeAction(Action):
    def __init__(self) -> None:
        self.url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'
        self.caminho_arquivo_csv = path.join(diretorio, 'cases-brazil-states.csv')
        return
    
    def name(self) -> Text:
        return 'action_responder_vacinados_na_cidade'
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        uf = tracker.get_slot('uf').upper()
        cidade = tracker.get_slot('cidade').capitalize()

        dataframe = pd.read_csv(self.url)

        dataframe['date'] = pd.to_datetime(dataframe['date'])

        dataframe_estado = dataframe.query(f"state == '{uf}'")[['date', 'vaccinated', 'vaccinated_second']]

        dataframe_estado_mais_recente = dataframe_estado.iloc[[-1]]

        data_mais_recente = dataframe_estado_mais_recente.iloc[0]['date'].strftime('%d/%m/%Y')
        vacinados = dataframe_estado_mais_recente.iloc[0]['vaccinated']

        message = f'Olha, até o dia {data_mais_recente} foram vacinadas {int(vacinados)} pessoas'

        dispatcher.utter_message(text=message)
        
        return []
