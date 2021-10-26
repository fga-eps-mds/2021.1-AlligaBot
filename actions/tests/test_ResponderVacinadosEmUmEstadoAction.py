import pytest
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from actions.ResponderVacinadosEmUmEstadoAction import ResponderVacinadosEmUmEstadoAction


class FakeDomain:
    def __init__(self):
        pass


class FakeTracker:
    def get_slot(self, slot):  
        pass

class ResponderVacinadosEmUmEstadoActionTest:

    def setup(self, mocker):
        self.service = ResponderVacinadosEmUmEstadoAction()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()


       

  
    def test_name(self, mocker):
        self.setup(mocker)
        assert self.service.name() == "action_responder_vacinados_em_um_estado"


    def test_bot(self,mocker):
        self.setup(mocker)
        mocker.patch.object(self.tracker,"get_slot",return_value="nao-existe")

        self.service.run(self.dispatcher,self.tracker,self.domain)
        print(self.dispatcher.messages[0])
        assert self.dispatcher.messages[0]['text'].startswith('Então... eu não achei o estado NAO-EXISTE')

        
def test_ResponderVacinadosEmUmEstadoAction(mocker):
    ResponderVacinadosEmUmEstadoActionTest().test_bot(mocker)
    ResponderVacinadosEmUmEstadoActionTest().test_name(mocker)