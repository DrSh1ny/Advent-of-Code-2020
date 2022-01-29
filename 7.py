def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        a.append(linha)
        linha=f.readline()
        
    f.close()
    return a



def CurateLine(linha):
    a={}
    linha=linha.split(" ")
    bag=linha[0]+" "+linha[1]
    if(linha[-3]=="no"):
        a[bag]=[]
    else:
        i=4
        lista=[]
        
        while(i<len(linha)):
            lista.append(linha[i]+" "+linha[i+1]+" "+linha[i+2])
            i+=4
        a[bag]=lista
    return a

def CountSh1ny(dict,bag,counter):
    counter=0
    for i in dict.keys():
        if(bag in dict[i]):
           
            counter+=1
            dict[i]=[]
            counter+=CountSh1ny(dict,i,counter)
            
            

    return counter

def CountSh1ny1(dict,bag):
    counter=0
    for i in dict[bag]:
        i=i.split(" ")
        numero=i[0]
        nome=i[1]+" "+i[2]

        
        
        total=int(numero) + int(numero)*CountSh1ny1(dict,nome)
        counter+=total
        
    
    return counter


def main():
    inp=ReadInput("7.txt")
    dict={}
    
    for linha in inp:
        bag=CurateLine(linha)
        dict.update(bag)

    
    print(CountSh1ny1(dict,"shiny gold"))

if __name__ == "__main__":
    main()