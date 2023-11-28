def fat(n):
  return 1 if n == 0 else n * fat(n-1)

def binario(n):
  return "" if n == 0 else binario(n//2) + str(n%2)

n = int(input("digite um valor: "))
f = 1
for i in range(1, n+1):
  f = f * i
print(n, "fatorial é", f, "ou recursivamente", fat(n), binario(f))
