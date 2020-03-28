import random
NOME=input("insira seu nome: ")
print("Bem vindo ao jogo Craps, {0}".format(NOME))
n=50
print("Para iniciar serão dadas {0} fichas para você".format(n))
Iniciar= False
while not Iniciar:
    Aposta_inicial= int(input('Faça sua aposta: '))
    if Aposta_inicial<= n:
        Iniciar=True
    else:
        print("aposta inválida; escolha um número de 0 a {0}". format(n))
        Iniciar= False
#fase Come out
escolhe_aposta=input("escolha o tipo de aposta:")
game_over=False
while not game_over:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma_dadosCO=(dado1+dado2)
    print(soma_dadosCO)
    if escolhe_aposta == "Pass Line Bet":
        if soma_dadosCO == 7 or soma_dadosCO == 11:
            print("Parabéns! você ganhou {0} fichas". format(Aposta_inicial))
            Aposta_inicial=Aposta_inicial*2
        elif soma_dadosCO == 2 or soma_dadosCO == 3 or soma_dadosCO == 12:
            print("Que pena, você tirou um craps! perca {0} fichas.". format(Aposta_inicial))
            print("game over")
            game_over=True
        else:
            point= soma_dadosCO
            print("Você passou para a fase Point")
#fase Point
    ganha_ou_perde=True
    while ganha_ou_perde:
        dado3=random.randint(1,6)
        dado4=random.randint(1,6)
        soma_dadosP=(dado3+dado4)
        print(soma_dadosP)
        if point == soma_dadosP:
            print("Você ganhou {0} fichas". format(Aposta_inicial))
            Aposta_inicial=Aposta_inicial*2
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