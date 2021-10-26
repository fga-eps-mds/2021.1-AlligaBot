import pytest
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from actions.ResponderSobreCovidAction import ResponderSobreCovidAction






class FakeDomain:
    def __init__(self):
        pass


class FakeTracker:
    def get_slot(self, slot):  
        pass




class ResponderSobreCovidActionTest:

    def setup(self, mocker):
        self.service = ResponderSobreCovidAction()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()

    def test_name(self,mocker):
        self.setup(mocker)
        assert self.service.name() == 'action_dados_covid_baseados_em_localizacao'

    def test_bot(self,mocker):
        self.setup(mocker)
        mocker.patch.object(self.tracker,"get_slot",return_value="nao-existe")

        self.service.run(self.dispatcher,self.tracker,self.domain)
        print(self.dispatcher.messages[0])
        assert self.dispatcher.messages[0]['text'].startswith('Não consegui encontrar o estado NAO-EXISTE 🥺. Lembre-se de informar somente a sigla, exemplo: DF 😉')


def test_ResponderVacinadosEmUmEstadoAction(mocker):
    ResponderSobreCovidActionTest().test_bot(mocker)
    ResponderSobreCovidActionTest().test_name(mocker)