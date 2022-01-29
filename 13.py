def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    linha=linha.strip("\n")
    valor=int(linha)
    linha=f.readline()
    linha=linha.strip("\n")
    linha=linha.split(",")
    linha=filter(lambda x: (x!="x") ,linha)
    linha=map(lambda x: int(x),linha)
    linha=list(linha)
    a.append(valor)
    a.append(linha)

    return a

def ReadInput1(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    linha=linha.strip("\n")
    valor=int(linha)

    linha=f.readline()
    linha=linha.strip("\n")
    linha=linha.split(",")
    b=[]
    for i in linha:
        if(i=="x"):
            b.append(1)
        else:
            b.append(int(i))
    a.append(valor)
    a.append(b)

    return a


def FindClosest(lista):
    horas=lista[0]
    ids=lista[1]

    id=0
    while(id==0):
        for bus in ids:
            if(horas%bus==0):
                id=bus
                return id,horas
        horas+=1
 
"""
def FindClosest1(buses):
        buses=buses[1]
        result = 1
        mode = 1
        for offset, bus_id in enumerate(buses):
            while (result + offset) % bus_id != 0:
                result += mode
            mode *= bus_id
        
        return result
""" 

def FindClosest2(lista):
    lista=lista[1]
    time=1
    salto=1
    atual=0
    
    while(atual<len(lista)):
        if (time+atual)%lista[atual]!=0:
            time+=salto
        else:
            salto*=lista[atual]
            atual+=1
    return time

def main():
    inp=ReadInput1("13.txt")
    print(inp)

    hora=FindClosest2(inp)
    print(hora)


    
    
    
    
    

    
if __name__ == "__main__":
    main()