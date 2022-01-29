import copy 
from functools import lru_cache
def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        linha=int(linha)
        a.append(linha)
        linha=f.readline()
        
    f.close()
    return a

def Sequence(lista):
    nova=copy.deepcopy(lista)
    seq=[]
    current=0
    while(nova!=[]):
        for addition in range(1,4):
            if(current+addition in nova):
                ind=nova.index(current+addition)
                seq.append(nova[ind])
                nova.pop(ind)
                current+=addition
                break
    return seq  

def JoltDif(seq):
    ones=0
    threes=0
    for i in range(len(seq)-1):
        if(seq[i+1]-seq[i]==1):
            ones+=1
            continue
        elif(seq[i+1]-seq[i]==3):
            threes+=1
            continue
    return ones,threes


def Sequence1(lista,seq,dif,last):
    #print(seq)
    nova=copy.copy(lista)
    seqNova=copy.copy(seq)
    #current ou é zero se estiver a comecar ou o ultimo da seq herdada
    if(seqNova!=[]):
        current=seqNova[-1]
    else:
        current=0
    
    #fazer escolha pedida e depois continuar branch
    ind=nova.index(current+dif)
    seqNova.append(nova[ind])
    nova.pop(ind)
    current+=dif

    #ran out of adapters?
    if(nova==[]):
        return [seqNova]
    
    upwards=[]
    #nao é possivel encontrar o proximo adapter
    if(min(nova)>current+3):
        return []
    #ja encontramos o ultimo que queriamos
    if(seqNova[-1]==last):
        return [seqNova]

    for i in range(1,4):
        if(current+i in nova):
            filhos=Sequence1(nova,seqNova,i,last)
            for filho in filhos:
                upwards.append(filho)

    
    return upwards

@lru_cache
def Sequence2(pointer):
    counter=0
    atual=inp[pointer]
    if(pointer==len(inp)-1):
        return 1
    for inc in range(1,4):
        if(atual+inc in inp[pointer+1:]):
            index=inp.index(atual+inc)
            counter+=Sequence2(index)
    return counter


inp=ReadInput("10.txt")
inp.sort()    
def main():
    
    print(inp)
    counter=0
    if(1 in inp):
        index=inp.index(1)
        counter+=Sequence2(index)
    if(2 in inp):
        index=inp.index(2)
        counter+=Sequence2(index)
    if(3 in inp):
        index=inp.index(3)
        counter+=Sequence2(index)


    print(counter)

    
if __name__ == "__main__":
    main()