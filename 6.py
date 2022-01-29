def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        grupo=""
        while(linha!='\n' and linha):
            grupo+=linha.strip("\n")
            linha=f.readline()

        a.append(grupo)
        linha=f.readline()
        
    f.close()
    return a

def ReadInput1(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        grupo=[]
        while(linha!='\n' and linha):
            grupo.append(linha.strip("\n"))
            linha=f.readline()

        a.append(grupo)
        linha=f.readline()
        
    f.close()
    return a

def UniqueSet(grupo):
    grupo=list(grupo)
    grupo=set(grupo)
    return grupo

def UniqueSet1(grupo):
    #print(grupo)
    count=0
    a=[]
    for pessoa in grupo:
        resp=list(pessoa)
        #print(resp)
        for letra in resp:
            a.append(letra)
    a=set(a)
    for i in a:
        all=1
        for pessoa in grupo:
            if(i not in pessoa):
                all=0
        if(all==1):
            count+=1
    
    return count

def main():
    inp=ReadInput1("6.txt")
    sum=0
    
    for i in inp:
        sum+=UniqueSet1(i)

    print(sum)

if __name__ == "__main__":
    main()