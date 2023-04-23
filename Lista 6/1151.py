n = int(input())
a = [0,1]
if n == 1:
  print('0')
elif n == 2:
  print('0 1')
else:
  for x in range(3, 1+n):
    a.append(a[x-3]+a[x-2])
    fibonacci = ' '.join(map(str, a))
  print(fibonacci)