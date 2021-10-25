import pytest

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from actions.ResponderVacinadosEmUmEstadoAction import ResponderVacinadosEmUmEstadoAction


def teste_nome():
    return ResponderVacinadosEmUmEstadoAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_dados_covid_baseados_em_localizacao'




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


        mocker.patch.object(self.dispatcher, "utter_message", return_value=None)

    @pytest.fixture
    def test_name(self, mocker):
        self.setup(mocker)
        assert self.service.name() == "action_responder_vacinados_em_um_estado"

    @pytest.fixture
    def test_test_ResponderVacinadosEmUmEstadoAction(mocker):
        ResponderVacinadosEmUmEstadoActionTest.test_name(mocker)