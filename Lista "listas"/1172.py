list = []
for i in range(10):
  a = int(input())
  list.append(a)
for i in range(10):
  if list[i] <= 0:
    list[i] = 1
  print(f'X[{i}] = {list[i]}')