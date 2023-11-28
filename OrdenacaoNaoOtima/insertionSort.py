def insertion(x):
  n = len(x)
  vz = 0
  for i in range(1, n):
    j = i
    while j > 0 and x[j] < x[j - 1]:
      vz = vz + 1
      x[j], x[j-1] = x[j-1], x[j]
      j = j - 1
  print("passou", vz)
  return x

x = [0,1,2,3,4,5,6,7,8,9]
print(insertion(x))
