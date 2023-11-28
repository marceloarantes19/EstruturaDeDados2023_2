def shell(x):
  h = 0
  n = len(x)
  while h < n:
    h = h * 3 + 1
  while h > 1:
    h = h // 3
    for i in range(h, n, h):
      j = i
      while j > 0 and x[j] < x[j - h]:
        x[j], x[j-h] = x[j-h], x[j]
        j = j - h
  return x

x = [9,8,7,10,4,15,18,22,33,44,55,21,20,13]
print(shell(x))
