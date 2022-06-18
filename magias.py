from random import randint
from funcoes_jogo import *

def d6():
    return randint(1, 6)

def d8():
    return randint(1, 8)

class BaseMagia():
    def __init__(self, jogador):
        self.jogador = jogador
        self.nome = 'NoName'
        self.custo_mp = 0
        self.dano = 0
        self.recuperacao_de_vida = 0
        self.recuperacao_de_vigor = 0
        self.valor = 5

    def __getitem__(self, item) -> tuple:
        return (self.nome, self.custo_mp, self.dano, self.recuperacao_de_vida, self.recuperacao_de_vigor)[item]

    def __str__(self):

        if self.dano > 0:
            return f'{self.nome}, Dano - {self.dano}'
        elif self.recuperacao_de_vida > 0:
            return f'{self.nome}, PV - {self.recuperacao_de_vida}'
        elif self.recuperacao_de_vigor > 0:
            return f'{self.nome}, Vigor - {self.recuperacao_de_vigor}'

class MagiaCura(BaseMagia):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.custo_mp = 2
        self.recuperacao_de_vida = (self.jogador.level * 2) + d6() + d6()
        self.nome = f"Cura"

class MagiaBolaDeFogo(BaseMagia):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.custo_mp = 3
        soma_do_dano = [d8() for i in range(1, 8)]
        self.dano = sum(soma_do_dano) + jogador.level
        self.nome = f'Bola de Fogo'

class MagiaMisseisMagicos(BaseMagia):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.custo_mp = jogador.level
        self.dano = d6()+(d6()*jogador.level)
        self.nome = f'Misseis Mágicos'

class MagiaExplosion(BaseMagia):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.nome = 'EXPLOSION'
        self.dano = 10000

def lista_de_magia_do_jogo(jogador):
    cura = MagiaCura(jogador)
    bola_de_fogo = MagiaBolaDeFogo(jogador)
    misseis_magicos = MagiaMisseisMagicos(jogador)
    explosion = MagiaExplosion(jogador)
    lista_de_magia = [
        cura, bola_de_fogo, misseis_magicos, explosion
    ]
    return lista_de_magia

if __name__ == '__main__':
    from personagem import Jogador, NPC
    p1 = Jogador('Jhony', 4)
    npc = NPC()
    lista_de_magia = lista_de_magia_do_jogo(p1)
    for magia in lista_de_magia:
        p1.adicionar_magia(magia)

    # def aprender_magia(jogador):
    #     for index, magia in enumerate(lista_de_magia):
    #         print(f'Lista -> [{index}]-[{magia[0]}]')
    #     opcao = int(input(': '))
    #     jogador.adicionar_magia(lista_de_magia[opcao])
    #
    # aprender_magia(p1)

    for magia in p1.magias_conhecidas:
        print(magia)

    print('*'*40)
    p1.usar_magia(p1.selecionar_magias(), npc)
    print(f'\033[31m{npc}\033[m')
    print(f'\033[34m{p1}\033[m')


    print('*'*40)
    p1.usar_magia(p1.selecionar_magias(), npc)
    print(f'\033[31m{npc}\033[m')
    print(f'\033[34m{p1}\033[m')
    print('*'*40)

    print(f'\033[31m{npc}\033[m')
    print(f'\033[34m{p1}\033[m')

