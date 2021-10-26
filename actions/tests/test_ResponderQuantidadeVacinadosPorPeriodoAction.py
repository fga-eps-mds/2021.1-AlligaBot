import pytest

from actions.ResponderQuantidadeVacinadosPorPeriodoAction import ResponderQuantidadeVacinadosPorPeriodoAction


def teste_nome():
    return ResponderQuantidadeVacinadosPorPeriodoAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_responder_quantidade_vacinados_por_periodo'