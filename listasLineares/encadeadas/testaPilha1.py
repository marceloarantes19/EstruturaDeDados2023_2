from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = input('Digite um nome: ')
j = 0
for i in x:
  j = j + 1
  elem = Elemento()
  elem.setNome(i)
  elem.setChave(j)
  n = No(elem)
  l.insereNoFim(n)
print('Lista do primeiro para o último:')
l.mostraLista()
estaciona = input("Pressione enter para seguir")
while not l.listaVazia():
  print(l.retiraNoInicio().getElemento().getNome())