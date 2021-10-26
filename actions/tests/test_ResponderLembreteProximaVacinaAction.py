import pytest
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from actions.ResponderLembreteProximaVacinaAction import ActionCadastrarLembrete, ActionLembrarUsuario 



class FakeDomain:
    def __init__(self):
        pass


class FakeTracker:
    def get_slot(self, slot):  
        pass



class ActionCadastrarLembreteTest:

    def setup(self, mocker):
        self.service = ActionCadastrarLembrete()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()

    def test_name(self,mocker):
        self.setup(mocker)
        assert self.service.name() == "action_cadastrar_lembrete_proxima_dose"


def test_ActionCadastrarLembrete(mocker):
     ActionCadastrarLembreteTest().test_name(mocker)


class ActionLembrarUsuarioTest:

    def setup(self, mocker):
        self.service = ActionLembrarUsuario()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()

    def test_name(self,mocker):
        self.setup(mocker)
        assert self.service.name() == "action_enviar_lembrete_da_proxima_dose_da_vacina"

def test_ActionLembrarUsuario(mocker):
     ActionLembrarUsuarioTest().test_name(mocker)