from inventario import lista_de_armas, Inventario
from magias import lista_de_magia_do_jogo

class LogaDoJogo:
    def __init__(self, jogador, inventario):
        self.jogador = jogador
        self.inventario = inventario
        self.lista_de_armas = lista_de_armas
        self.lista_de_magias = lista_de_magia_do_jogo(jogador)

    def comprar_item(self):
        print(f'Moedas = {self.jogador.moeda}')
        print('Escolha uma arma.')

        try:
            for indice, arma in enumerate(self.lista_de_armas):
                print(f'Moedas - {arma.valor}')
                print(f'[({indice})-{arma}]')
            escolha = int(input(': '))
            arma = self.lista_de_armas[escolha]
            if self.jogador.moeda >= arma.valor:
                print(f'Equipar {arma} ?')
                opcao = int(input('[1]-sim [2]-nao : '))
                if opcao == 1:
                    if self.jogador.arma is None:
                        self.jogador.equipar_arma(self.lista_de_armas[escolha])
                    else:
                        print('ja tinh a uma arma')
                        self.inventario.adicionar_items(self.jogador.arma)
                        self.jogador.equipar_arma(self.lista_de_armas[escolha])
                if opcao == 2:
                    self.inventario.adicionar_items(self.lista_de_armas[escolha])
                self.jogador.moeda -= arma.valor
            else:
                print('Moedas insuficientes')
        except:
            self.jogador.arma = None
        print()

    def aprender_magia(self):
        print(f'Moedas = {self.jogador.moeda}')
        print('Escolha sua Magia.')
        try:
            lista_de_magia = lista_de_magia_do_jogo(self.jogador)
            print('[0] Atualizar Loja')
            for index, magia in enumerate(lista_de_magia):
                print(f' -> Valor {magia.valor}g\n'
                      f'    [{index+1}]-[{magia}]')
            opcao = int(input(': '))
            if opcao == 0:
                self.aprender_magia()
            if self.jogador.moeda >= lista_de_magia[opcao-1].valor:
                self.jogador.adicionar_magia(lista_de_magia[opcao-1])
        except:
            pass


    def vender_magia(self):
        print('Escola a magia para vender.')
        for index, magia in enumerate(self.jogador.magias_conhecidas):
            print(f' -> [{index}]-[{magia}')
        opcao = int(input(': '))
        self.jogador.remover_magia(opcao)

