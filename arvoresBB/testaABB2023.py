from Elemento import Elemento
from NoABB import NoABB 
from ArvoreBB import ArvoreBB

arv = ArvoreBB()
x = int(input("Digite um valor para a chave (-1 para sair): "))
while x != -1:
  e = Elemento(x)
  n = NoABB(e)
  arv.insereNo(n)
  arv.visitaEmOrdem(arv.getRaiz())
  x = int(input("Digite um valor para a chave (-1 para sair): "))


