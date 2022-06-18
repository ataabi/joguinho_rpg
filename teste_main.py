from personagem import *
from inventario import *

p1 = Jogador("Play", 4)
mochila = Inventario(p1)
print(p1)

mochila.adicionar_items('Espada')
mochila.adicionar_items('Espada+1')
mochila.adicionar_items('Espada+2')
mochila.adicionar_items(lista_de_armas[2])

for item in mochila:
    print(item)

print("#"*50)
print(mochila)