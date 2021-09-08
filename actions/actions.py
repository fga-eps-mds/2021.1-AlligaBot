from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class JokeAction(Action):
    def name(self) -> Text:
        return "action_joke"

    def run(
        self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        req = requests.get(
            'https://official-joke-api.appspot.com/jokes/random').json()
        setup = req['setup']

        punchline = req['punchline']
        dispatcher.utter_message(text=setup)
        dispatcher.utter_message(text=punchline)
        return []
