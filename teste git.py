import random
NOME=input("insira seu nome: ")
print("Bem vindo ao jogo Craps {0}".format(NOME))
n=50
print("Para iniciar serão dadas {0} fichas para você".format(n))
#fase Come out
Iniciar= False
while not Iniciar:
    Aposta_inicial= int(input('Faça sua aposta: '))
    if Aposta_inicial<= n:
        Iniciar=True
    else:
        print("aposta inválida; escolha um número de 0 a {0}". format(n))
        Iniciar= False
dado1=random.randint(1,6)
dado2=random.randint(1,6)
soma_dadosCO=(dado1+dado2)
print(soma_dadosCO)
