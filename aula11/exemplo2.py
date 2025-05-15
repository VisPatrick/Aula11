
# try:

#     n1 = float(input('\nNúmero: '))
#     n2 = float(input('Numero: '))
#     div = n1 / n2
#     print(div)


# except ZeroDivisionError as e:
#     print(30*'=')
#     print(f'Não pode dividir por 0 - {e}')

#   Exemplo 02
try:

    n1 = float(input('\nNúmero: '))
    n2 = float(input('Numero: '))
    div = n1 / n2
    print(div)


except ZeroDivisionError as e:
    print(30*'=')
    print(f'Não pode dividir por 0 - {e}')

except ValueError as e:
    print(30*'=')
    print(f'Não digite por extenso - {e}')