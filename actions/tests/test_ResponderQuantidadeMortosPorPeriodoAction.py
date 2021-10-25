import pytest

from actions.ResponderQuantidadeMortosPorPeriodoAction import ResponderQuantidadeMortosPorPeriodoAction

def teste_nome():
    return ResponderQuantidadeMortosPorPeriodoAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_responder_quantidade_mortos_por_periodo'