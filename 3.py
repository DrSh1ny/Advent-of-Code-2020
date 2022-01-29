def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n")
        linha=list(linha)
        a.append(linha)
        linha=f.readline()
    f.close()
    return a

def PrintPath(lista):
    for i in lista:
        print(i)

def ExtendPath(lista,listaOG):
    nova=[]
    for i in range(len(listaOG)):
        linha=lista[i]
        linhaOG=listaOG[i]
        comp=len(linhaOG)
        for i in range(comp):
            linha.append(linhaOG[i])
        nova.append(linha)  
    return nova


def Move(lista,posX,posY):
    if(lista[posY][posX]=="."):
        lista[posY][posX]="O"
    else:
        lista[posY][posX]="X"

def CheckCrashes(lista):
    count=0
    for i in lista:
        for j in i:
            if(j=="X"):
                count+=1
    return count


def checkSlope(ficheiro,incX,incY):
    inp=ReadInput(ficheiro)
    og=ReadInput(ficheiro)


    posX=0
    posY=0

    while(posY<len(inp)):
        if(posX>=len(inp[0])):
            inp=ExtendPath(inp,og)

        Move(inp,posX,posY)
        posX+=incX
        posY+=incY

    return CheckCrashes(inp)

def main():
    mult=1

    mult=mult*checkSlope("3.txt",1,1)
    mult=mult*checkSlope("3.txt",3,1)
    mult=mult*checkSlope("3.txt",5,1)
    mult=mult*checkSlope("3.txt",7,1)
    mult=mult*checkSlope("3.txt",1,2)

    print(mult)

if __name__ == "__main__":
    main()