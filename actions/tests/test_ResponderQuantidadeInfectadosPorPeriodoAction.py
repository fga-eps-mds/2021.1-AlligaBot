import pytest


from actions.ResponderQuantidadeInfectadosPorPeriodoAction import ResponderQuantidadeInfectadosPorPeriodoAction


def teste_nome():
    return ResponderQuantidadeInfectadosPorPeriodoAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_responder_quantidade_infectados_por_periodo'