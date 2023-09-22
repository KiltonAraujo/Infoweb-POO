def aprovado(nota1, nota2):
  media = (nota1 + nota2) / 2
  if media >= 60:
    print(f"Média: {media:.0f}")
    print('Aluno aprovado')
  else:
    print(f'Média: {media:.0f}')
    print("Aluno reprovado")
nota1, nota2 = map(int,input().split())
aprovado(nota1,nota2)