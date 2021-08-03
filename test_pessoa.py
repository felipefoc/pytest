import pytest
import sys
sys.path.append("..")
from models.pessoa import Pessoa, Pessoas


def test_verificar_fixture(criar_pessoas):
    lista = criar_pessoas[3].lista[0]
    assert len(lista) == 3
    assert lista[0].nome == 'Felipe'
    assert lista[1].nome == 'Gustavinho'
    assert lista[2].nome == 'Rubi'

def test_verifica_se_fixture_nao_esta_ativa():
    assert pytest.raises(NameError)

def test_criar_pessoa(criar_pessoas):
    lista = criar_pessoas[3].lista[0]
    p = Pessoa._criar_pessoa()
    lista.append(p)
    assert lista[-1].nome == p.nome
    assert lista[-1].sexo == p.sexo
    assert lista[-1].idade == p.idade
    assert len(lista) == 4

def test_remover_pessoa(criar_pessoas):
    lista = criar_pessoas[3].lista[0]
    lista.remove(lista[0])
    assert len(lista) == 2

@pytest.mark.parametrize("nome", ['Maria', 'Carlos'])
@pytest.mark.parametrize("idade", [18, 22])
def test_parametrizer_pessoa(nome, idade):
    pessoa1 = Pessoa(nome=nome, sexo='Feminino', idade=idade)
    pessoa2 = Pessoa(nome=nome, sexo='Masculino', idade=idade)
    assert pessoa1.nome == nome
    assert pessoa1.idade == idade
    assert pessoa2.nome == nome
    assert pessoa2.idade == idade
    