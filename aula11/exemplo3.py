try:    # try é o bloco que pode gerar erro

    n1 = float(input('\nNúmero: '))
    n2 = float(input('Numero: '))
    resultado = n1 / n2   


except ZeroDivisionError as e:  # exceção específica # as e é o erro que ocorreu
    print(30*'=')
    print(f'Não pode dividir por 0 - {e}')

else:
    print(f'Oresultadoé: {resultado}')

finally:    # finally é sempre executado
    print('Fim da operação!!')

#   EXEMPLO - 04
try:    # try é o bloco que pode gerar erro

    n1 = float(input('\nNúmero: '))
    n2 = float(input('Numero: '))
    resultado = n1 / n2   

except ZeroDivisionError, ValueError as e:  # exceção específica # as e é o erro que ocorreu
    print(30*'=')
    print(f'Erro, voçê digitou o número por extenso - {e}')

else:
    print(f'Oresultadoé: {resultado}')

finally:    # finally é sempre executado
    print('Fim da operação!!')

#   EXEMPLO - 05
try:

    n1 = float(input('\nNúmero: '))
    n2 = float(input('Numero: '))
    resultado = n1 / n2   


except Exception as e:
    print(30*'=')
    print(f'Erro, voçê digitou o número por extenso - {e}')

else:
    print(f'Oresultadoé: {resultado}')

finally:
    print('Fim da operação!!')