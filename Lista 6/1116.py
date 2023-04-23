t = int(input())
for x in range(t):
    a,b = map(int,input().split())
    if b != 0:
        nica = a / b
        print(f'{nica}')
    else:
        print('divisao impossivel')