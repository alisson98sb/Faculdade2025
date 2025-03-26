import re

def test_senha_segura():
    assert senha_segura("Senha123!") == True
    assert senha_segura("senhafraca") == False
    assert senha_segura("SENHA123!") == False
    assert senha_segura("Senha!") == False