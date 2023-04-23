base = int(input())
altura = int(input())

area = base * altura
p = (base + altura) * 2
diagonal = ((base ** 2) + (altura ** 2)) ** 0.5

print(f'''Área: {area:.2f}
Perímetro: {p:.2f}
Diagonal: {diagonal:.2f}''')