from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB
x = [4, 3, 10, 1, 9, 11, 6]
a = ArvoreBB()
for i in x:
  e = Elemento(i)
  n = NoABB(e)
  a.insereNo(n)
a.visitaEmOrdemInv(a.getRaiz())
b = a.encontra(a.getRaiz(), 6)
if b != None:
  print(b.getInfo().getValores())
else:
  print("Chave Não encontrada")

print(a.lenArvore(a.getRaiz()), " - ", a.somaArvore(a.getRaiz()))
print("Menor:", a.menorValor(a.getRaiz()).getInfo().getValores())
print("Maior:", a.maiorValor(a.getRaiz()).getInfo().getValores())

a.mostraNivel()
  
