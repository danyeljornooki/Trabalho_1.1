# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (
# resto da divisão).
num = float(input("Escreva um número: "))
resto = num % 2

if resto == 0:
    print(f"O número {num:.0f} é par")
else:
    print(f"O número {num:.0f} é  impar")
