cueio = 0
rato = 0
sapo = 0
total = 0
a = int(input())
for x in range(a):
    tik,tok = input().split()
    tik = int(tik)
    if tok == 'C':
        cueio += tik
        total += tik
    if tok == 'R':
        rato += tik
        total += tik 
    if tok == 'S':
        sapo += tik
        total += tik
sapos = (sapo / total) * 100
ratos = (rato / total) * 100
coelhos = (cueio / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {cueio}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {coelhos:.2f} %')
print(f'Percentual de ratos: {ratos:.2f} %')
print(f'Percentual de sapos: {sapos:.2f} %')