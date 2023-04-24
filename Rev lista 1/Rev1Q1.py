a = int(input())
b = int(input())
c = int(input())
d = int(input())

med = (a+b+c+d) / 4
print(f'Média = {med}')
print('Números menores que a média')
if a <= 6:
  print(a)
if b <= 6:
  print(b)
if c <= 6:
  print(c)
if d <= 6:
  print(d)

print('Números maiores ou iguais que a média')
if a >= 6:
  print(a)
if b >= 6:
  print(b)
if c >= 6:
  print(c)
if d >= 6:
  print(d)