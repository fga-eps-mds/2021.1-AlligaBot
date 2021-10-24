import pytest


from actions.ResponderVacinadosEmUmEstadoAction import ResponderVacinadosEmUmEstadoAction


def teste_nome():
    return ResponderVacinadosEmUmEstadoAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_responder_vacinados_em_um_estado'