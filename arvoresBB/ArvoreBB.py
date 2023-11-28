from Elemento import Elemento
from NoABB import NoABB
class ArvoreBB:
  def __init__(self):
    self.__raiz = None
  def getRaiz(self):
    return self.__raiz 
  def setRaiz(self, r):
    self.__raiz = r
  def arvoreVazia(self):
    return self.getRaiz() == None
  def insereNo(self, n = NoABB()):
    if self.arvoreVazia():
      self.setRaiz(n)
    else:
      self.insere(None, self.getRaiz(), n)
  def insere(self, pai, atual, n):
    if atual == None: # preciso inserir o nó
      if n.getInfo().getChave()<pai.getInfo().getChave():
        pai.setFilhoE(n)
      else:
        pai.setFilhoD(n)
    elif n.getInfo().getChave()<atual.getInfo().getChave():
      self.insere(atual, atual.getFilhoE(), n)
    else:
      self.insere(atual, atual.getFilhoD(), n)
  def retiraNo(self, ch):
    ret = None
    if not self.arvoreVazia():
      ret = self.retira(None, self.getRaiz(), ch)
    return ret 
  def retira(self, pai, atual, ch):
    if atual == None: # Não encontrou elemento na árvore
      return None
    elif ch < atual.getInfo().getChave(): # Procurado é menor que a chave atual
      return self.retira(atual, atual.getFilhoE(), ch)
    elif ch > atual.getInfo().getChave(): # Procurado é maior que a chave atual
      return self.retira(atual, atual.getFilhoD(), ch)
    else: # Encontrou o elemento a remover da árvore
      if not atual.temDoisFilhos():
        # Remoções triviais
        if atual.eFolha():
          if pai == None: # atual é o último nó da árvore
            self.setRaiz(None)
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(None)
          else:
            pai.setFilhoD(None)
        elif atual.soTemFilhoAEsquerda():
          if pai == None:
            self.setRaiz(atual.getFilhoE())
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(atual.getFilhoE())
          else:
            pai.setFilhoD(atual.getFilhoE())
          atual.setFilhoE(None)
        else:
          if pai == None:
            self.setRaiz(atual.getFilhoD())
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(atual.getFilhoD())
          else:
            pai.setFilhoD(atual.getFilhoD())
          atual.setFilhoD(None)
        return atual
      # Remoção não trivial
      else:
        return self.simulaRemocao(atual, atual, atual.getFilhoE())
  def simulaRemocao(self, fixo, pai, atual):
    if atual.getFilhoD() != None:
      return self.simulaRemocao(fixo, atual, atual.getFilhoD())
    else:
      x = fixo.getInfo()
      fixo.setInfo(atual.getInfo())
      atual.setInfo(x)
      if fixo == pai:
        pai.setFilhoE(atual.getFilhoE())
        atual.setFilhoE(None)
      else:
        pai.setFilhoD(atual.getFilhoE())
        atual.setFilhoE(None)
      return atual
  def visitaPreOrdem(self, n):
    if n != None:
      print(n.getInfo().getValores())
      self.visitaPreOrdem(n.getFilhoE())
      self.visitaPreOrdem(n.getFilhoD())
  def visitaEmOrdem(self, n):
    if n != None:
      self.visitaEmOrdem(n.getFilhoE())
      print(n.getInfo().getValores())
      self.visitaEmOrdem(n.getFilhoD())
  def visitaEmOrdemInv(self, n):
    if n != None:
      self.visitaEmOrdemInv(n.getFilhoD())
      print(n.getInfo().getValores())
      self.visitaEmOrdemInv(n.getFilhoE())
  def visitaPosOrdem(self, n):
    if n != None:
      self.visitaPosOrdem(n.getFilhoE())
      self.visitaPosOrdem(n.getFilhoD())
      print(n.getInfo().getValores())
  def mostraArvore(self, n, niv):
    if n != None:
      sn = ""
      for i in range(0, niv):
        sn = sn +"   |"
      sn = sn + "--"
      print(sn,n.getInfo().getChave())
      self.mostraArvore(n.getFilhoE(), niv+1)
      self.mostraArvore(n.getFilhoD(), niv+1)

    f = []
    f.append(self.getRaiz())
    while len(f) > 0:
      atual = f.pop(0)
      print(atual.getInfo().getChave())
      if atual.getFilhoE() != None:
        f.append(atual.getFilhoE())
      if atual.getFilhoD() != None:
        f.append(atual.getFilhoD())
  
  #Metodo para encontrar um valor na arvore
  def encontra(self, n, ch):
    if n != None:
      print("Chave Atual: ", n.getInfo().getChave())
      if ch == n.getInfo().getChave():
        return n
      elif ch < n.getInfo().getChave():
        return self.encontra(n.getFilhoE(), ch)
      else:
        return self.encontra(n.getFilhoD(), ch)
    return None

  def lenArvore(self, n):
    return 0 if n == None else 1 + self.lenArvore(n.getFilhoE()) + self.lenArvore(n.getFilhoD())
  
  def lenArvore2(self, n):
    ret = 0
    if n != None:
      x = self.lenArvore2(n.getFilhoE())
      y = self.lenArvore2(n.getFilhoD())
      ret = 1 + x + y
    return ret

  def somaArvore(self, n):
    ret = 0
    if n != None:
      x = self.somaArvore(n.getFilhoE())
      y = self.somaArvore(n.getFilhoD())
      ret = n.getInfo().getChave() + x + y
    return ret
  
  def menorValor(self, n):
    if n.getFilhoE() != None:
      return self.menorValor(n.getFilhoE())
    return n

  def maiorValor(self, n):
    if n.getFilhoD() != None:
      return self.maiorValor(n.getFilhoD())
    return n
  
  def mostraNivel(self):
    f = []
    nv = []
    f.append(self.getRaiz())
    nv.append(0)
    while len(f) > 0:
      n = f.pop(0)
      k = nv.pop(0)
      print(n.getInfo().getValores(), "Nivel:", k)
      if n.getFilhoE()!=None:
        f.append(n.getFilhoE())
        nv.append(k+1)
      if n.getFilhoD()!=None:
        f.append(n.getFilhoD())
        nv.append(k+1)

