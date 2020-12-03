
def funcao (*num) :
    maior = 0
    menor = num[0][0]

    tamanho = len(num[0])

    for i in range(0, tamanho):
        if num[0][i] > maior :
            maior = int(num[0][i])
    
        if num[0][i] < menor :
            menor = int(num[0][i])
    
        return maior, menor

numeros = list()
op = 1
while op != 0:
    print("digite zero (0) para sair ")
    op = int(input())
    if op != 0:
        numeros.append(op)

print(funcao(numeros))