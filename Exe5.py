# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (
# codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros = float(input("Escreva a quantidade de litros gastos: "))
tipo = input("Qual combustível usado a = álcool, g = gasolina: ")
if tipo == "a":
    if litros <= 20:
        litros = litros * 1.90
        desconto = (litros * 3) / 100
        print(f"O valor pago é de R${litros - desconto:.2f}.")
    else:
        desconto = (litros * 5) / 100
        print(f"O valor pago é de R${litros - desconto:.2f}.")
elif tipo == "g":
    litros = litros * 2.50
    if litros <= 20:
        desconto = (litros * 4) / 100
        print(f"O valor pago é de R${litros - desconto:.2f}.")
    else:
        desconto = (litros * 6) / 100
        print(f"O valor pago é de R${litros - desconto:.2f}.")
else:
    print("Digitou algo errado.")