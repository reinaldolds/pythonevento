cadastrar = input("Deseja cadastrar (s/n)? ")
if cadastrar:
    nome_produto = input("qual produto? ")
    quantidade_estoque = int(input("quantidade em estoque? "))
    preco_venda = float(input("qual preço? "))

    dados = [nome_produto, quantidade_estoque, preco_venda]

    print(dados)
    quantidade_pagar = int(input("quantas vai querer? "))
    apagar = float(input("qual valor vair ser pago? "))
    
    divida = quantidade_pagar * preco_venda
    troco = apagar - divida

    def calcular_troco():
        if apagar > preco_venda:
            print(f'Você pagou {apagar} e seu troco é de:', troco)
        elif apagar == preco_venda:
            print(f'Obrigado pela compra!')
        elif apagar < preco_venda:
            print(f'Dinheiro insuficiênte.')
        else:
            print(f'Algo deu errado!')
    
    calcular_troco()

else:
    print("ok, sem produto para cadastrar.")