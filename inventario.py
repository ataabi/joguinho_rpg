class Arma:
    def __init__(self, nome, dano, dado, valor):
        self.aprimoramento = 0
        self.nome = nome
        self.dano = dano
        self.dado = dado
        self.valor = valor

    def __str__(self):
        return f'{self.nome} | Dano-{self.dano} Dados-{self.dado} +{self.aprimoramento}'

    def __getitem__(self, item):
        lista = [self.dano, self.dado]
        return lista[item]

    def dano_da_arma(self):
        return self.dado

    def dados_adicionais(self):
        return self.dado

    def aprimorar_armar(self):
        self.aprimoramento += 1
        if self.aprimoramento % 2 == 0:
            self.dado += 1
        elif self.aprimoramento % 2 >= 1:
            self.dano += 5

class Inventario:
    def __init__(self, jogador):
        self._jogador = jogador
        self._items = []
        self._fragmento_de_pergaminho = 0
        self._moeda = 10

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return self._items

    def escolher_item(self):
        for i, item in enumerate(self._inventario):
            print(f'[{i+1}]-[{item}]')
        opcao = int(input(': '))
        return self._inventario[opcao - 1]

    def adicionar_items(self, item):
        self._items.append(item)

    def trocar_arma(self, jogador):
        arma = self.escolher_item()
        jogador.equipar_arma(arma)
        del arma

    @property
    def items(self) -> list:
        return [item for item in self._items]



espada_curta = Arma('Espada Curta', 5, 2, 10)
espada_longa = Arma('Espada Longa', 10, 1, 10)
arco_curto = Arma('Arco Curto', 3, 3, 10)
arco_longo = Arma('Arco Longo', 5, 2, 10)
espada_HK = Arma("Killer",200,10, 0)

lista_de_armas = [espada_longa, espada_curta,
                  arco_curto, arco_longo, espada_HK]

