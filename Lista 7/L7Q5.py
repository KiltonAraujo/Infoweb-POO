print("Digite seu nome completo.")
def formatar_nome(nome):
  s = input().lower
  nome = s.split()
  resultado = ""
  for ini in nome:
      resultado += ini[0].upper
      resultado += ini[1:]
      resultado += ""
  print(resultado)

s = input().lower
nome = s.split()