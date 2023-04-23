i = []
c = 0
p = 0
for x in range(0,100):
  a = int(input())
  i.append(a)
  if i[x] > c:
    c = i[x]
    p = x + 1

print(c)
print(p)