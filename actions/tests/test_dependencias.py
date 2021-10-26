import sys
import pkg_resources


def test_tensorflow_instalado():
    pacote_instalados = [i.key for i in list(pkg_resources.working_set)]
    texto = "tensorflow-text" in pacote_instalados

    if sys.platform == "win32":
        assert not texto
