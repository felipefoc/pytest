from dataclasses import dataclass
from faker import Faker
import random

fake = Faker()

sex = ['Feminino', 'Masculino']

@dataclass
class Pessoas:
    """ Classe Pessoas """
    lista: list

@dataclass
class Pessoa:
    """ Classe Pessoa """
    nome: str
    sexo: str
    idade: int

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return self.nome
    
    def _criar_pessoa():
        return Pessoa(fake.name(), random.choice(sex), random.randint(10, 99))