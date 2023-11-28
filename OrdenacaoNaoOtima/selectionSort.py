def selection(x):
  n = len(x)
  vz = 0
  for i in range(0, n-1):
    for j in range(i+1, n):
      vz = vz + 1
      if x[j]<x[i]:
        x[i], x[j] = x[j], x[i]
  print("Passou", vz)
  return x

k = [0,1,2,3,4,5,6,7,8,9]
print(selection(k))
