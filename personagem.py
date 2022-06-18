from random import randint

def d6():
    return randint(1, 6)

def d8():
    return randint(1, 8)

class Personagem:
    def __init__(self, nome, atributo):
        self._atributo = atributo
        self._nome = nome

        self._pontos_de_vida = 100
        self._pontos_de_vida_max = 100

        self._pontos_de_magia = 10
        self._pontos_de_magia_max = 10

        self._pontos_de_vigor = 100
        self._pontos_de_vigor_max = 100

        self._level = 1
        self.arma = None

    @property
    def nome(self):
        return self._nome

    # Manipulação da Vida
    @property
    def vida(self):
        return self._pontos_de_vida
    @property
    def vida_maxima(self):
        return self._pontos_de_vida_max

    def set_vida(self, valor):
        if self._pontos_de_vida <= self._pontos_de_vida_max:
            self._pontos_de_vida += valor
        elif self._pontos_de_vida > self._pontos_de_vida_max:
            self._pontos_de_vida = self._pontos_de_vida_max

    # Manipulação do MP(Pontos de magia)
    @property
    def mp(self):
        return self._pontos_de_magia
    @property
    def mp_maximo(self):
        return self._pontos_de_magia_max

    def set_mp(self, valor):
        if self._pontos_de_magia > self._pontos_de_magia_max:
            self._pontos_de_magia = self._pontos_de_magia_max
        elif self._pontos_de_magia <= self._pontos_de_magia_max:
            self._pontos_de_magia += valor

    # Manipulação do Vigor
    @property
    def vigor(self):
        return self._pontos_de_vigor
    @property
    def vigor_maximo(self):
        return self._pontos_de_vigor_max

    def set_vigor(self, valor):
        if self._pontos_de_vigor > self._pontos_de_vigor_max:
            self._pontos_de_vigor = self._pontos_de_vigor_max
        elif self._pontos_de_vigor <= self._pontos_de_vigor_max:
            self._pontos_de_vigor += valor

    # Manipulação do Level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, valor):
        self._level = valor

    @property
    def atributo(self):
        return self._atributo

    def ataque(self, npc):
        numero_de_rolagens = d6()

        if self._pontos_de_vigor <= 0:
            print('Você está cansado')
        else:
            if self.arma == None:
                if self._atributo == numero_de_rolagens:
                    npc._pontos_de_vida -= 6 # Acerto Critico
                    print(f'Acerto Critico - Dano [{4}]')
                elif self._atributo < numero_de_rolagens:
                    npc._pontos_de_vida -= 3 # Acerto Normal
                    print(f'Acerto - Dano [{2}]')
                else:
                    print('Errou')

            if self.arma:
                dano, numero_de_rolagens = self.arma
                for i in range(numero_de_rolagens):
                    rolagem = d6()
                    if rolagem == self._atributo:
                        npc._pontos_de_vida -= dano * 2 # Acerto Critico
                        print(f'Acerto Critico - Dano [{dano * 2}]')
                    elif rolagem < self._atributo:
                        npc._pontos_de_vida -= dano # Acerto Normal
                        print(f'Acerto - Dano [{dano}]')
                    else:
                        print('Errou')

        self._pontos_de_vigor -= 1

    def usar_magia(self, magia, alvo=False):
        nome, custo_mp, dano, vida, vigor = magia
        print(nome,end=' ')
        if self.mp >= custo_mp:
            self.set_vida(vida)
            self.set_vigor(vigor)
            self.set_mp(-custo_mp)
            print(vida)
        if alvo:
            print('Dano ', dano)
            alvo.set_vida(-dano)

        elif self.mp < custo_mp:
            print('MP insuficiente')

class Jogador(Personagem):
    def __init__(self, nome, atributo):
        super().__init__(nome, atributo)
        self._inventario = []
        self._exp = 0  # exp = experiencia
        self.exp_up = int((10 + self._level) * (self._level * 1.12))
        self.skill_points = 2 # Pontos de Habilidade
        self._lista_de_magias = []

    def __str__(self):
        return (f'Nome - {self.nome} Lv({self.level})'
                f'\nPV-[{self._pontos_de_vida}/{self._pontos_de_vida_max}]'
                f' MP-[{self._pontos_de_magia}/{self._pontos_de_magia_max}]'
                f'\nVigor-[{self._pontos_de_vigor}/{self._pontos_de_vigor_max}]'
                f' Atributo-[{self.atributo}]'
                f'\nGold-[??] EXP-[{self.exp}/{self.exp_up}]'
                f'\nArma = [{self.arma}]')

    def descansar(self):
        self.set_vida(10)
        self.set_vigor(10)
        self.set_mp(4)

    # Ajustes do Vigor do Jogador
    def vigor_upgrade(self):
        if self.skill_points >= 1:
            self._pontos_de_vigor_max += 5
            self._pontos_de_vigor = self._pontos_de_vigor_max
            self.skill_points -= 1
        else:
            print('Pontos de Habilidades Insuficientes')

    # Ajustes do Pontos de Magia do Jogador
    def mp_upgrade(self):
        if self.skill_points >= 1:
            self._pontos_de_magia_max += 2
            self._pontos_de_magia = self._pontos_de_magia_max
            self.skill_points -= 1
        else:
            print('Pontos de Habilidades Insuficientes')

    # Ajustes do Pontos de Vida do Jogador
    def vida_upgrade(self):
        if self.skill_points >= 1:
            self._pontos_de_vida_max += 5
            self._pontos_de_vida = self._pontos_de_vida_max
            self.skill_points -= 1
        else:
            print('Pontos de Habilidades Insuficientes')

    # Ajustes dos Pontos de Experiencia do jogador
    @property
    def exp(self):
        return self._exp

    def set_exp(self, valor):
        self._exp += valor

    # Ajuste do Level do jogador
    def level_up(self):
        self._level += 1
        self.exp_up = int((10 + self._level) * (self._level * 1.12))
        self.skill_points += 2
        self._pontos_de_vida_max += 10
        self._pontos_de_vida = self._pontos_de_vida_max
        self._pontos_de_magia_max += 2
        self._pontos_de_magia = self._pontos_de_magia_max
        self._pontos_de_vigor_max += 3
        self._pontos_de_vigor = self._pontos_de_vigor_max
        print(f'Level UP ({self.level-1})>({self.level})')

    def verifica_level(self):
        if self._exp >= self.exp_up:
            self.level_up()

    # Ajustes das Magias do Jogador
    def adicionar_magia(self, magia):
        self._lista_de_magias.append(magia)

    def remover_magia(self, index):
        del self._lista_de_magias[index]

    @property
    def magias_conhecidas(self):
        return self._lista_de_magias

    def selecionar_magias(self):
        for index, magia in enumerate(self._lista_de_magias):
            print(index, ' - ', magia)
        opcao = int(input(': '))
        return self.magias_conhecidas[opcao]

    # ajustes de equipamentos
    def equipar_arma(self, arma):
        self.arma = arma

class NPC(Personagem):
    def __init__(self):
        super().__init__(
            nome='NPC', atributo=randint(2, 5))

        self.moeda = randint((self.level-1), (self.level+2))

        adicional = 10 * self.level
        self._pontos_de_vida = 100 + adicional
        self._pontos_de_vida_max = 100 + adicional

        adicional = 2 * self.level
        self._pontos_de_magia = 10 + adicional
        self._pontos_de_magia_max = 10 + adicional

        adicional = 3 * self.level
        self._pontos_de_vigor = 100 + adicional
        self._pontos_de_vigor_max = 100 + adicional

    def muda_level(self, jogador):
        menor = jogador.level - 2 #level_do_jogador_
        maior = jogador.level + 2 #level_do_jogador_
        self.level = randint(menor, maior)

    def __str__(self):
        return f'NPC Lv{self.level}\n' \
               f'PV-{self.vida}/{self.vida_maxima} MP-{self.mp}/{self.mp_maximo}'


# class Ferreiro:

