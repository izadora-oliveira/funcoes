def gorjeta (conta, p = 10) :

    gorjeta = (conta * p)/100
    print("gorjeta do garçon: ", gorjeta)
    print("sua conta : ", conta)
    print("valor final: ", conta + gorjeta)

op = 1
while op != 0:
    print("0- para sair digite zero")
    print("1- pagar com gorjeta")
    print("2- pagar sem gorjeta ")
    op = int(input())

    if op == 1 :
        conta = int(input("valor da conta: "))
        print(gorjeta(conta))

    if op == 2 :
        conta = int(input("valor da conta: "))
        print("valor final : ", conta)