# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?"
# "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" O programa
# deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente
# a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente".
print("Responda só com (s) ou (n)")
p1 = input("Telefonou para a vítima?")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")

if p1 == "s":
    p1 = 1
else:
    p1 = 0
if p2 == "s":
    p2 = 1
else:
    p2 = 0
if p3 == "s":
    p3 = 1
else:
    p3 = 0
if p4 == "s":
    p4 = 1
else:
    p4 = 0
if p5 == "s":
    p5 = 1
else:
    p5 = 0
r1 = p1 + p2 + p3 + p4 + p5
if r1 == 0 or r1 == 1:
    print("É inocente")
elif r1 == 2:
    print("É Suspeito")
elif r1 == 3 or 4:
    print("É Cúmplice")
elif r1 == 5:
    print("É Assasino")
