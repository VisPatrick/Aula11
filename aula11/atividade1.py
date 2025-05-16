# #   crie um programa que peça duas notas ao usuario, caulcule a média e informe se o aluno foi aprovado

try:
    nota1 = float(input('\nDigite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except ValueError as e:
    print(f'Digite apenas número: {e}')
else:
    # processamento
    if nota1 in range(0, 10) and nota2 in range(0, 10):
        media = (nota1 + nota2) / 2
        print(f'\nSua média foi: {media}')

        # saida
        if media >= 6:
            print(f'Aluno aprovado:{media}')
        else:
            print(f'Aluno Reprovado: {media}')
    else:
        print(30*'*')
        print('Precisa está no intervalo de 0 - 10')
finally:
    print(30*'=')
    print('Verificado com sucesso')