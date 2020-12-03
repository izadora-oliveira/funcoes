#funcao para definir o maior e menor
def funcao (*num) :
    maior = 0
    menor = num[0][0]
    
    for i in range(0, len(num[0])) :
        if num[0][i] > maior :
            maior = int(num[0][i])
    
        if num[0][i] < menor :
            menor = int(num[0][i])
    return maior, menor
    
#loop para pegar todos os numeros
numeros = list()
op = 1
while op != 0:
    print("digite zero (0) para sair ")
    op = int(input())
    if op != 0:
        numeros.append(op)
#chamando a funcao
print(funcao(numeros))