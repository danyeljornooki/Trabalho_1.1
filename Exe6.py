# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                     Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
pm = 2.50
pma = 1.80
kgm = float(input("Escreva quantos Kg de morangos: "))
kgma = float(input("Escreva quantos Kg de Maçã: "))

if kgm >= 5:
    totalmg = (pm - 0.3) * kgm
else:
    totalmg = pm * kgm
if kgma >= 5:
    totalmga = (pma - 0.3) * kgma
else:
    totalmga = pma * kgma
if (totalmg + totalmga > 25) or (kgma + kgm > 8):
    des = ((totalmga + totalmg) * 10) / 100
    resul = totalmga + totalmg - des
else:
    resul = totalmga + totalmg
print(f"O preço final é de R${resul:.2f}")
