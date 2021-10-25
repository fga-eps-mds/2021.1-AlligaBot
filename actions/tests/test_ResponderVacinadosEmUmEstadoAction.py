import pytest
from rasa_sdk.executor import CollectingDispatcher

from actions.ResponderVacinadosEmUmEstadoAction import ResponderVacinadosEmUmEstadoAction

class FakeDomain:
    def __init__(self):
        pass


class FakeTracker:
    def get_slot(self, slot):  
        pass


class test_ResponderVacinadosEmUmEstadoAction:

    def setup(self, mocker):
        self.service = ResponderVacinadosEmUmEstadoAction()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()


    def teste_nome():
        return ResponderVacinadosEmUmEstadoAction()

    @pytest.fixture
    def test_name(teste_nome):
        name = teste_nome.name()
        assert name == 'action_responder_vacinados_em_um_estado'

    def test_responder_vacinados_estado(dispatcher: CollectingDispatcher,self,mocker):
        self.setup(mocker)
        mocker.patch().object(self.tracker,"get_slot",return_value="nao-existe")

        self.service.run(self.dispatcher, self.tracker, self.domain)

        assert 'Então... eu nao achei o estado nao-existe' in dispatcher.messages[0]['text']