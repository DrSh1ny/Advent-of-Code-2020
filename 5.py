import math

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

def MidOf(Lower,Upper):
    meio=(Upper-Lower)/2+Lower
    return math.floor(meio),math.floor(meio)

def Move(step,LR,UR,LC,UC):
    #print(LR)
    #print(UR)
    #print(LC)
    #print(UC)
    #print("\n")
    a,b=MidOf(LR,UR)
    c,d=MidOf(LC,UC)
    if(step=="F"):
        return LR,a,LC,UC
    if(step=="B"):
        return b,UR,LC,UC
    if(step=="L"):
        return LR,UR,LC,c
    if(step=="R"):
        return LR,UR,d,UC

    
    return LR,UR,LC,UC
    
def PrintPlane(lista):
    for i in range(len(lista)):
        print(lista[i],end="")
        print(i)

def main():
    inp=ReadInput("5.txt")
    max=0
    
    a=[["O" for i in range(8)] for i in range(128)]


    for seat in inp:
        LR=0
        UR=128
        LC=0
        UC=7

        for i in seat:
            LR,UR,LC,UC=Move(i,LR,UR,LC,UC)

        result=LR*8 + UC
        if(result>max):
            max=result
        
        a[LR][UC]="X"

    print(max)
    PrintPlane(a)

if __name__ == "__main__":
    main()