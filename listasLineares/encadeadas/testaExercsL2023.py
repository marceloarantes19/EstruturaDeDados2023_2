from Lista import Lista
from Elemento import Elemento
from No import No
l = Lista()
for i in range(0, 5):
  e = Elemento(i)
  n = No(e)
  l.insereNoFim(n)

l.mostraLista()
p = int(input("Digite um número (-1 para terminar): "))
while p != -1:
  e = Elemento(i+p)
  n = No(e)
  l.insereNaPosicao(n, p)
  l.mostraLista()
  p = int(input("Digite um número (-1 para terminar): "))

# Teste de Remocao
p = int(input("Digite um número (-1 para terminar): "))
while p != -1:
  n = l.retiraNaPosicao(p)
  if n!=None:
    print("Saindo:", n.getElemento().getValores(), "\n")
  l.mostraLista()
  p = int(input("Digite um número (-1 para terminar): "))

l.limpaListaReal(l.getCabeca())
print("Elementos na Lista:", l.lenLista())
