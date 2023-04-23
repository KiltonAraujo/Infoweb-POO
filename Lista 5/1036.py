a,b,c = map(float, input().split())
delta = (b ** 2) - (4 * a) * c
if delta == 0 or delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    
    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')