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
r1 = p1 + p2 + p3 + p4 + p5

if r1 == "nnnnn":
    print("Inocente")
elif r1 == "snnnn":
    print("Inocente")
elif r1 == "ssnnn":
    print("Suspeito")
elif r1 == "sssnn":
    print("Cumplice")
elif r1 == "ssssn":
    print("Cúmplice")
elif r1 == "sssss":
    print("Assasino")
else:
    print("Escreveu algo errado.")
