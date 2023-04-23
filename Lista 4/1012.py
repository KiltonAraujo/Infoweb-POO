A,B,C = map(float, input().split())
aT = (A * C) / 2
PI =  3.14159
aC = PI * C ** 2
aTz = ((A + B) * C) / 2
aQ = B ** 2
aR = A * B
print(f'TRIANGULO: {aT:.3f}')
print(f'CIRCULO: {aC:.3f}')
print(f'TRAPEZIO: {aTz:.3f}')
print(f'QUADRADO: {aQ:.3f}')
print(f'RETANGULO: {aR:.3f}')