palavra = str(input("Digite a palavra: "))
cont = 0
for i in palavra:
    if i.upper() == 'A':
        cont +=1
    else:
        cont += 0
if cont > 0:
    print(f"A palavra tem letra 'a' e aparece {cont}.")
else:
    print(f"A palavra não tem letra 'a'")