# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
# da operação deve ser acompanhado de uma frase que diga se o número é:
num1 = float(input("Escreva um número: "))
num2 = float(input("Escreva um número: "))
resposta = float(input("\nPara saber se é par ou impar digite (1)"
                       "\nPara saber se é positivo ou negativo digite (2)"
                       "\nPara saber se é inteiro ou decimal digite (3)"
                       "\nEscolha uma operaçaõ deseja fazer:"))
# par ou ímpar;
if resposta == 1:
    resto1 = num1 % 2
    if resto1 == 0:
        print(f"O número {num1:.0f} é par")
    else:
        print(f"O número {num1:.0f} é  impar")
    resto2 = num2 % 2
    if resto2 == 0:
        print(f"O número {num2:.0f} é par")
    else:
        print(f"O número {num2:.0f} é  impar")

# positivo ou negativo;
elif resposta == 2:
    if num1 >= 0:
        print(f'{int(num1)} é um número positivo')
    else:
        print(f'{int(num1)} é um número negativo')
    if num2 >= 0:
        print(f'{int(num2)} é um número positivo')
    else:
        print(f'{int(num2)} é um número negativo')
# inteiro ou decimal.
elif resposta == 3:
    if round(num1):
        print(f'{int(num1)} é um número inteiro')
    else:
        print(f'{num1} é um número decimal')
    if round(num2):
        print(f'{int(num2)} é um número inteiro')
    else:
        print(f'{num2} é um número decimal')
