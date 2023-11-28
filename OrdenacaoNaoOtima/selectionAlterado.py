def selection(x):
  n = len(x)
  for i in range(0, n-1):
    trocou = False
    m = i
    for j in range(i+1, n):
      if x[j]<x[m]:
        trocou = True
        m = j
    if not trocou:
      break
    x[i], x[m] = x[m], x[i]
  return x

k = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(selection(k))
