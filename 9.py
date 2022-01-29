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

def Combinations(lista):
    combo=[]

    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            combo.append([lista[i],lista[j]])

    return combo

def FindSequence(lista,magicN):
    pointer=0
    lenght=1
    while(1):
        if(pointer+lenght>=len(lista)):
            pointer+=1
            lenght=1

        seq=lista[pointer:pointer+lenght]

        if(sum(seq))>magicN:
            pointer+=1
            lenght=1
        
        if(sum(seq)==magicN):
            return seq
        
        lenght+=1
    return -1

        

def main():
    inp=ReadInput("9.txt")
    preamble=25
    #magicN=127
    magicN=1038347917
    
    pointer=preamble
    while(pointer<len(inp)):
        combo=Combinations(inp[pointer-preamble:pointer])
        combo=list(map(lambda x: x[0]+x[1],combo))
        if(inp[pointer] not in combo):
            print(inp[pointer])
        pointer+=1
    
    seq=FindSequence(inp,magicN)
    seq.sort()
    print(seq)

if __name__ == "__main__":
    main()