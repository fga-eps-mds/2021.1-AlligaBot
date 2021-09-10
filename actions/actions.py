# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


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

    req = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    setup = req['setup']

    punchline = req['punchline']
    dispatcher.utter_message(text=setup)
    dispatcher.utter_message(text=punchline)
    return []
