class Market:
    i = 1
    a = 0
    prod = [0]*9999
    tipo = [0]*9999
    preço = [0]*9999
    qtdpeso = [0]*9999
    SubTotal = [0]*9999
    PreçoTotal = 0
    while(i>0):
        print("Digite o nome do Produto: ")
        prod[a] = input()
        print("Digite o tipo do produto: ")
        tipo[a] = input()
        print("Digite o preço do produto: ")
        preço[a] = float (input())
        print("Digite a quantidade/peso do produto: ")
        qtdpeso[a] = float (input())
        
        SubTotal[a] = qtdpeso[a] * preço[a]
        
        PreçoTotal = PreçoTotal + SubTotal[a]
        
        a = a + 1
        
        print("")
        print("Digite 1 para continuar ou 0 para sair.")
        i = int (input())
    
    print("")
    print("")
    
    n = 0
    while(n<a):
        print("Nome do Produto: ",prod[n])
        print("Tipo do Produto: ",tipo[n])
        print("Preço do Produto: R$%.2f " % preço[n])
        print("Quantidade do produto vendido: ",qtdpeso[n])
        print("SubTotal do produto: R$%.2f " % SubTotal[n])
        
        print("")
        
        n = n + 1
    
    print("")
    print("Preço Total de todos os produtos vendidos: R$%.2f " % PreçoTotal)
    
    print("")
    print("Digite o valor a ser pago")
    val_pag = float (input())
    if(val_pag>PreçoTotal):
        troco = val_pag - PreçoTotal
        print("Troco: R$%.2f " % troco)
        


    
    
    
    