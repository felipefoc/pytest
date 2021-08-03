import sys
sys.path.append(".")
from models.pessoa import Pessoa, Pessoas
from pytest import fixture

@fixture(scope='function')
def criar_pessoas():
    p1 = Pessoa('Felipe', 'Masculino', 27)
    p2 = Pessoa('Gustavinho', 'Masculino', 30)
    p3 = Pessoa('Rubi', 'Feminino', 18)
    pessoas = Pessoas([])
    pessoas.lista.append([p1, p2, p3])

    print(f'{p1.nome}, {p2.nome}, {p3.nome} foram criados...')
    return p1, p2, p3, pessoas