def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("digite peso em kg:"))
altura = float(input("digite a altura em metros:"))

#trocar imc = peso / (altura ** 2)
imc = calcular_imc(peso, altura)

print(imc)