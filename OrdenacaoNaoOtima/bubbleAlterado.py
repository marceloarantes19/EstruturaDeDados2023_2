def bubble(x):
  n = len(x)
  for i in range(0, n-1):
    trocou = False
    for j in range(n - 1, i, -1):
      if x[j - 1] > x [j]:
        trocou = True
        x[j - 1], x[j] = x[j], x[j - 1]
    if not trocou:
      break
  return x

k = []
n = 10
for i in range(0, n):
  k.append(i)
print(bubble(k))
