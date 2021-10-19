import pytest
from os import path
from datetime import datetime
from typing import Any, Text, Dict, List


# from actions import ResponderSobreCovidAction
# from actions.ResponderSobreCovidAction import ResponderSobreCovidAction
from actions.actions import ResponderSobreCovidAction

def teste_nome():
    return ResponderSobreCovidAction()

@pytest.fixture
def test_name(teste_nome):
    name = teste_nome.name()
    assert name == 'action_dados_covid_baseados_em_localizacao'
