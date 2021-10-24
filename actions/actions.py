# -*- coding: utf-8 -*-

import os
import time
import requests
import requests
import patoolib
import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from os import path
from typing import Any, Text, Dict, List

from .ResponderVacinadosEmUmEstadoAction import ResponderVacinadosEmUmEstadoAction
from .ResponderSobreCovidAction import ResponderSobreCovidAction
from .ResponderLembreteProximaVacinaAction import ActionCadastrarLembrete, ActionLembrarUsuario 
from .ResponderQuantidadeInfectadosPorPeriodoAction import ResponderQuantidadeInfectadosPorPeriodoAction
from .ResponderQuantidadeMortosPorPeriodoAction import ResponderQuantidadeMortosPorPeriodoAction
from .ResponderQuantidadeVacinadosPorPeriodoAction import ResponderQuantidadeVacinadosPorPeriodoAction

