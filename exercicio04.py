produto_nome = input("qual produto? ")
quantidade = int(input("qual a quantidade? "))
preco = float(input("valor de venda?"))
pagamento = int(input("qual valor vai pagar? "))
apagar = quantidade * preco
troco = pagamento - preco

if pagamento > apagar:
    print(f'O preço de {produto_nome} é: {apagar} e seu troco é de: {troco} obrigado pela compra!')
elif pagamento == apagar:
    print(f'Obrigado pela compra!')
else:
    print(f'O preço de {produto_nome} é: {apagar} e o valor esta incompleto.')