def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        if(linha[1]=="a"):
            mask=linha[7:]
            a.append(mask)
        else:
            linha=linha.split(" ")
            address=int(linha[0][4:-1])
            value=int(linha[2])
            a.append([address,value])
        linha=f.readline()
    return a



def Operator(mask,value):
    mask1=""
    mask0=""
    
    for i in mask:
        if(i=="X"):
            mask1+="0"
            mask0+="1"
        if(i=="1"):
            mask1+="1"
            mask0+="1"
        if(i=="0"):
            mask1+="0"
            mask0+="0"
    
    mask1=int(mask1,base=2)
    mask0=int(mask0,base=2)

    value='{0:036b}'.format(value)
    value=int(value,base=2)

    novo=value | mask1
    novo= novo & mask0
    return novo

def Operator1(mask,address):
    novos=[]
    address='{0:036b}'.format(address)
    out=""
    inicial=""

    for i in range(36):
        if(mask[i]=="1"):
            out+="1"
            inicial+="1"
        elif(mask[i]=="0"):
            out+=address[i]
            inicial+=address[i]
        elif(mask[i]=="X"):
            out+="X"
            inicial+="0"

    inicial=int(inicial,base=2)
    novos.append(inicial)

    #print(out)
    for i in range(36):
        if(out[i]=="X"):
            soma=pow(2,36-i-1)
            #print(36-i-1,soma)
            naddresses=list(map(lambda x: x+soma,novos))
            for j in naddresses:
                novos.append(j)
    #print(novos)
    return novos

def main():
    inp=ReadInput("14.txt")
    print(inp)

    dic={}
    mask=""

    """
    for i in inp:
        if(len(i)!=2):
            mask=i
            
        else:
            valor=Operator(mask,i[1])
            dic[i[0]]=valor
    print(dic)

    sum=0
    """
    for i in inp:
        if(len(i)!=2):
            mask=i
            
        else:
            address=Operator1(mask,i[0])
            for j in address:
                dic[j]=i[1]
    #print(dic)

    sum=0
    
    for i in dic.keys():
        sum+=dic[i]
    print(sum)
if __name__ == "__main__":
    main()