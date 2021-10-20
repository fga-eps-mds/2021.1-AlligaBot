import pytest


from actions.ResponderSobreCovidAction import ResponderSobreCovidAction


def teste_nome():
    return ResponderSobreCovidAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_dados_covid_baseados_em_localizacao'