from funcoes_jogo import chama_numero, criar_personagem, batalhar
from personagem import Personagem, save, load
import PySimpleGUI as sg
from random import randint

class TelaPython:
    def __init__(self):
        #layout
        layout_inicial = [
            [sg.Button('Novo Jogo')],
            [sg.Button('Continuar')]
        ]
        # janela
        janela = sg.Window('RPG SIMPLES').layout(layout_inicial)
        # Extração dos dados na tela
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()


# Menu incial
print('[1] - Novo Jogo\n'
      '[2] - Continuar')
escolha = chama_numero()
if escolha == 1:
    jogador = criar_personagem()
    save(jogador, 1)
elif escolha == 2:
    jogador = load(1)

