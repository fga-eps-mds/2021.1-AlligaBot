from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, ReminderScheduled, ReminderCancelled
from os import path
from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

class ActionCadastrarLembrete(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_cadastrar_lembrete_proxima_dose"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dia = tracker.get_slot("dia")
        mes = tracker.get_slot("mes")
        ano = tracker.get_slot("ano")

        QTD_SEGUNDOS_EM_UM_DIA = 86400

        data_final_informada = f'{dia}-{mes}-{ano}'

        data_inicial = datetime.strptime(datetime.today().strftime('%d-%m-%Y'), '%d-%m-%Y')
        data_final = datetime.strptime(data_final_informada, '%d-%m-%Y')

        quantidade_dias = abs((data_final - data_inicial).days)
        quantidade_segundos = quantidade_dias * QTD_SEGUNDOS_EM_UM_DIA

        dispatcher.utter_message(f"Eu lembrarei você na data de {data_final_informada}")

        date = datetime.now() + timedelta(seconds=quantidade_segundos)
        entities = tracker.latest_message.get("entities")

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionLembrarUsuario(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_enviar_lembrete_da_proxima_dose_da_vacina"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(f"Hoje é o dia {dia}/{mes}/{ano} 🥳, lembre-se de ir ao posto de saúde para tomar a outra dose da vacina do Covid-19")

        return []