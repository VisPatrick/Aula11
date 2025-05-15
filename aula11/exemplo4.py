print('\n=== CAIXA ELETRÔNICO ==')
print(25*'=')

while True:

    try:
        saldo = 1000
        saque = float(input('\nInforme o valor de saque: '))

    except ValueError as e:
        print(f'Digite apenas número: {e}')

    else:
        if saque > 0:
            if saldo >= saque:
                saldo -= saque
                break
            elif saque > saldo:
                print('Saldo insuficiente')

        else:
            print('O saque precisa ser maior que 0')

    finally:
        print('Operação Finalizada')

    print(f'\nSeu saldo é de: {saldo}')