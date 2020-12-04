def convert_palavra(*b) :
    invertida = list()
    for i in range(0, len(b[0])) :
        invertida.append(b[0][i][::-1])

    for i in range(0, len(b[0])) :
        if b[0][i] == invertida[i] :
            print(invertida[i])

a = list()
palavra = 'a'
while palavra != 's' :
    
    print("para sair digite ('s')")
    palavra = input("digite uma palavra: ")
    if palavra != 's' and 'S' :
        if palavra in a :
             print("ja tem essa palavra")
        else:
            a.append(palavra)
            
    else:
        pass

convert_palavra(a)



