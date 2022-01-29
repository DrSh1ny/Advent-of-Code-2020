import math
def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        op=linha[0]
        value=linha[1:]
        a.append([op,int(value)])
        linha=f.readline()
    return a


def Move(posX,posY,degree,instruc):
    opcode=instruc[0]
    value=instruc[1]

    if(opcode=="N"):
        posY+=value
    if(opcode=="S"):
        posY-=value
    if(opcode=="E"):
        posX+=value
    if(opcode=="W"):
        posX-=value

    if(opcode=="L"):
        degree+=value
    if(opcode=="R"):
        degree-=value
    
    if(opcode=="F"):
        aux=math.radians(degree)
        posX+=round(math.cos(aux)*value)
        posY+=round(math.sin(aux)*value)

    return posX,posY,degree

def Move1(posX,posY,wposX,wposY,instruc):
    opcode=instruc[0]
    value=instruc[1]

    if(opcode=="N"):
        wposY+=value
    if(opcode=="S"):
        wposY-=value
    if(opcode=="E"):
        wposX+=value
    if(opcode=="W"):
        wposX-=value

    if(opcode=="L"):
        value=float(math.radians(value))
        aux1=wposX*math.cos(value)-wposY*math.sin(value)
        aux2=wposX*math.sin(value)+wposY*math.cos(value)
       
        wposX=round(aux1)
        wposY=round(aux2)

    if(opcode=="R"):
        value=float(math.radians(-value))
        aux1=wposX*math.cos(value)-wposY*math.sin(value)
        aux2=wposX*math.sin(value)+wposY*math.cos(value)

        wposX=round(aux1)
        wposY=round(aux2)

    if(opcode=="F"):
        for i in range(value):
            posX+=wposX
            posY+=wposY

    return posX,posY,wposX,wposY

def main():
    inp=ReadInput("12.txt")
    print(inp)
    
    posX=0
    posY=0
    wposX=10
    wposY=1
    for i in inp:
        posX,posY,wposX,wposY=Move1(posX,posY,wposX,wposY,i)
        print(posX,posY,wposX,wposY)
    print(abs(round(posX))+abs(round(posY)))
    
    
    

    
if __name__ == "__main__":
    main()