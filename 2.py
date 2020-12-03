def contagens (inicio, fim, passo) :
    if inicio < fim :
        i= inicio
        while i <= fim :
            print(f'{i}', end=' ')
            i += passo

        print()

    elif inicio > fim :
        i= inicio
        while i >= fim :
            print(f'{i}', end=' ')
            i -= passo
        
        print()

    else :
        i = inicio
        while i != fim :
            print(f'{i}', end=' ')
            i += passo

print("de 1 ate 10, de 1 em 1")
contagens(1, 10, 1)
print()
print("de 10 ate 0, de 2 em 2")
contagens(10, 0, 2)
print()
print("defina inicio, fim e o passo: ")
i= int(input("inicio: "))
f= int(input("fim: "))
p= int(input("passo: "))
contagens(i, f, p)