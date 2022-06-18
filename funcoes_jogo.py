from personagem import *
from random import randint
from inventario import lista_de_armas, Inventario
from magias import *
import pickle
from loja import LogaDoJogo

def chama_numero(mensagem=': ', mensagem_de_alerta="Ação inválida"):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except:
            print(mensagem_de_alerta)
    return numero

def menu(lista_de_menus:list):
    for menu in lista_de_menus:
        pass

def linha_entre_menus():
    print()
    print('\033[32m*\033[m'*80)

def menu_inical():
    linha_entre_menus()
    print('[1] - Novo Jogo\n'
          '[2] - Continuar')
    while True:
        escolha = chama_numero()
        if escolha == 1:
            # jogador = criar_personagem()
            jogador = Jogador('Play', 4)
            inventario_jogador = Inventario(jogador)
            save(jogador, 1)
            save(inventario_jogador, 'inventario')
            return (jogador, inventario_jogador)

        elif escolha == 2:
            jogador = load(1)
            inventario_jogador = load('inventario')
            return (jogador, inventario_jogador)
        else:
            print('Opção inválida')

def menu_princial(jogador, inventario):
    linha_entre_menus()
    while True:
        print(f'Jogador: {jogador.nome} Lv({jogador.level})\n'
              f'PV-{jogador.vida}/{jogador.vida_maxima} MP-{jogador.mp}/{jogador.mp_maximo} '
              f'Vigor-{jogador.vigor}/{jogador.vigor_maximo}')
        print('Ações: ')
        print('[1]-Batalhar [2]-Aprimorar [3]-Personagem\n'
              '[4]-Loja! [5]-INN(2 Moedas) [6]-Sair')
        acao = chama_numero()

        if acao == 1:
            batalhar(jogador)
        elif acao == 2:
            menu_de_compras_de_atributos(jogador)
        elif acao == 3:
            menu_do_jogador(jogador, inventario)
        elif acao == 4:
            menu_da_loja(jogador, inventario)
        elif acao == 5:
                jogador.descansar()

        elif acao == 6:
            save(jogador, 1)
            break
        save(jogador, 1)
        save(inventario, 'inventario')

def menu_do_jogador(jogador, inventario):
    linha_entre_menus()
    print(jogador, '\n')
    print('[0]-Voltar [1]-Inventario \n'
          '[2]-Grimório [3]-Trocar Equipamento')
    opcao = chama_numero()
    if opcao == 0:
        menu_princial(jogador, inventario)
    if opcao == 1:
        print("Inventario - ", len(inventario))
        for item in inventario:
            print('    ', item)
    if opcao == 2:
        print('Grimório-')
        for magia in jogador.magias_conhecidas:
            print(magia)

def menu_de_compras_de_atributos(jogador):
    linha_entre_menus()
    while jogador.skill_points > 0:
        print(f'Pontos de Atributos = {jogador.skill_points}\n'
              f'Atributos:\n'
              f'[1]PV + 5 | [2]MP + 2| [3]Vigor + 5\n[0] Sair')
        escolha = chama_numero()
        if escolha == 1:
            jogador.vida_upgrade()
        elif escolha == 2:
            jogador.mp_upgrade()
        elif escolha == 3:
            jogador.vigor_upgrade()
        elif escolha == 0:
            break

def menu_de_batalha(jogador):
    linha_entre_menus()
    if jogador.nome != "NPC":
        print(f'\033[32m{jogador.nome}\033[m ({jogador.level})')
    else:
        print(f"\033[31m{jogador.nome}\033[m ({jogador.level})")

    print(f'PV({jogador.vida}/{jogador.vida_maxima}) . MP({jogador.mp}/{jogador.mp_maximo}) . '
              f'Vigor({jogador.vigor}/{jogador.vigor_maximo})'
              f'\nArma equipada ({jogador.arma})\n')

def batalhar(jogador, inventario):
    linha_entre_menus()
    npc = NPC()
    npc.arma = lista_de_armas[randint(0, 3)]
    npc.muda_level(jogador)
    while True:
        # Status do Personagem
        print('*'*40)
        menu_de_batalha(jogador)
        menu_de_batalha(npc)
        # para o jogo se a vida do personagem for iqual a 0(zero)
        if jogador.vida <= 0 or jogador.vigor <= 0:
            print('Você Morreu !!!')
            jogador.set_exp(-10)
            inventario.moeda -= 1
            jogador.verifica_level()
            break
        if npc.vida <= 0:
            print('VOCÊ VENCEU !!!')
            jogador.set_exp(10)
            jogador.moeda += npc.moeda
            jogador.verifica_level()
            break
        # Menu de Batalha
        else:
            print('[0]-Fugir [1]-Atacar [2]-Especial')
            escolha_de_batalha = chama_numero('Ação: ')
            print('*'*40)

            if escolha_de_batalha == 0:
                break

            elif escolha_de_batalha == 1:
                print(jogador.nome.title())
                jogador.ataque(npc)
                print('NPC')

            elif escolha_de_batalha == 2:
                jogador.usar_magia(jogador.selecionar_magias(), npc)

            npc.ataque(jogador)

def menu_da_loja(jogador, inventario):
    linha_entre_menus()
    loja = LogaDoJogo(jogador, inventario)
    print('[1]-Armas [2]-Magias [3]-Vender')
    opcao = chama_numero()
    if opcao == 1:
        loja.comprar_item()
    elif opcao == 2:
        loja.aprender_magia()
    elif opcao == 3:
        loja.vender_magia()

def criar_personagem():
    nome = input('Nome: ') .title().lstrip()
    print('Quanto Maior seu Atributo Mais forte e resistente sera seu personagem\n'
          'Quanto Menor seu Atributo mais perspicaz e inteligente sera seu personagem\n'
          'Escolha um valor entre 2~5 ou 0 para um valor aleatório.')
    print('Escolha seu atributo: ')
    atributo_escolhido = chama_numero()
    if atributo_escolhido >= 2 and atributo_escolhido <= 5:
        return Jogador(nome, atributo_escolhido)
    elif atributo_escolhido == 0:
        return Jogador(nome, randint(3, 5))
    else:
        print('Não foi possivel criar o Personagem ')

def save(personagem,slot):
    try:
        with open(f'save_{slot}.json', 'wb') as save_file:
            pickle.dump(personagem, save_file)
    except:
        open('log.json', 'x')

def load(slot):
    with open(f'save_{slot}.json', 'rb') as load_file:
        return pickle.load(load_file)







