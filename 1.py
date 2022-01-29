def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    linha=f.readline()
    while(linha):
        linha=int(linha)
        a.append(linha)
        linha=f.readline()
    f.close()
    return a

def CalSum(lista,MagicNumber):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(i==j):
                continue
            if(lista[i]+lista[j]==MagicNumber):
                return i,j
    return -1,-1

def CalSum1(lista,MagicNumber):
    for i in range(len(lista)):
        for j in range(len(lista)):
            for k in range(len(lista)):
                index=[i,j,k]
                if len(index) > len(set(index)):
                    continue
                if(lista[i]+lista[j]+lista[k]==MagicNumber):
                    return i,j,k
    return -1,-1,-1


def main():
    star=2020
    inp=ReadInput("1.txt")
    print(inp)
    a,b,c=CalSum1(inp,2020)
    print(a)
    print(b)
    print(c)
    print(inp[a])
    print(inp[b])
    print(inp[c])
    print(inp[a]*inp[b]*inp[c])




if __name__ == "__main__":
    main()
    