import random
NOME=input("insira seu nome: ")
print("Bem vindo ao jogo Craps, {0}".format(NOME))
n=50
print("Para iniciar serão dadas {0} fichas para você".format(n))
Iniciar= False
game_over=False
while not game_over:
    while not Iniciar:
        Aposta_inicial= int(input('Faça sua aposta: '))
        if Aposta_inicial<= n:
            Iniciar=True
        else:
            print("aposta inválida; escolha um número de 0 a {0}". format(n))
            Iniciar= False
    #fase Come out
    escolhe_aposta=input("escolha o tipo de aposta:")
    if escolhe_aposta == "Pass Line Bet":
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        soma_dadosCO=(dado1+dado2)
        print(soma_dadosCO)
        if soma_dadosCO == 7 or soma_dadosCO == 11:
            print("Parabéns! você ganhou {0} fichas". format(Aposta_inicial))
            Saldo=Aposta_inicial*2 + (n-Aposta_inicial)
        elif soma_dadosCO == 2 or soma_dadosCO == 3 or soma_dadosCO == 12:
            print("Que pena, você tirou um craps! perca {0} fichas.". format(Aposta_inicial))
            print("game over")
            game_over=True
        else:
            point=soma_dadosCO
            print("Você passou para a fase Point")
    #fae Point
        ganha_ou_perde=True
        while ganha_ou_perde:
                dado3=random.randint(1,6)
                dado4=random.randint(1,6)
                soma_dadosP=(dado3+dado4)
                print(soma_dadosP)
                if point == soma_dadosP:
                    print("Você ganhou {0} fichas". format(Aposta_inicial))
                    Saldo=Aposta_inicial*2 + (n-Aposta_inicial)
                    recomeçar=input("O jogo acabou. Deseja recomeçar?")
                    ganha_ou_perde=False
                    game_over=True
                elif soma_dadosP == 7:
                    print ("Você perdeu {0} fichas.". format(Aposta_inicial))
                    print("game over")
                    game_over=True
                    ganha_ou_perde=False
                else:
                    print("Try again")
    if escolhe_aposta== 'field' or 'Field':
        dado5=random.randint(1,6)
        dado6=random.randint(1,6)
        soma_dadosF= (dado5+dado6)
        print(soma_dadosF)
        if soma_dadosF== 3 or 4 or 9 or 10 or 11:
            print('você ganhou {0} fichas'.format(Aposta_inicial))
            Saldo= Aposta_inicial*2 + (n-Aposta_inicial)
        elif soma_dadosF== 2:
            print('você ganhou {0} fichas'.format(Aposta_inicial*2))
            Saldo=  Aposta_inicial*3 + (n-Aposta_inicial)
        elif soma_dadosF== 12:
            print('você ganhou {0} fichas'.format(Aposta_inicial*3))
            Saldo=  Aposta_inicial*4 + (n-Aposta_inicial)
        else:
            print('você perdeu {0} fichas'.format(Aposta_inicial))
            Saldo= (n-Aposta_inicial)
    print(Saldo)