def calcular_imc(nome, idade, peso, altura):
    imc = peso / (altura ** 2)
    return imc

nome = input("Digite o Nome? ")
idade = int(input("Digite idade? "))
peso = float(input("digite peso em kg:"))
altura = float(input("digite a altura em metros:"))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("obsidade GRAU I")
elif 35 <= imc < 39.9:
    print("obesidade GRAU II")
else:
    print("obsidade GRAU III")

#trocar imc = peso / (altura ** 2)
imc = calcular_imc(nome, idade, peso, altura)

print(imc)