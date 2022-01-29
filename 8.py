import copy 
def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        novo=[linha,0]
        a.append(novo)
        linha=f.readline()
        
    f.close()
    return a

def decode(combo):
    combo=combo.split(" ")
    opcode=combo[0]
    value=int(combo[1])

    return opcode,value

def execute(lista):
    contador=0
    pointer=0

    while(pointer<len(lista)):
        if(lista[pointer][1]!=0):
            return contador,0

        opcode,value=decode(lista[pointer][0])

        if(opcode=="nop"):
            lista[pointer][1]+=1
            pointer+=1
            continue
        elif(opcode=="acc"):
            lista[pointer][1]+=1
            pointer+=1
            contador+=value
        elif(opcode=="jmp"):
            lista[pointer][1]+=1
            pointer+=value

    return contador,1
        
def TrialError(lista):
    
    for i,linha in enumerate(lista):
        nova=copy.deepcopy(lista)
        opcode,value=decode(linha[0])

       
        if(opcode=="jmp"):
            nova[i][0]="nop "+str(value)
            cont,loop=execute(nova)

            
            if(loop==1):
                return cont
        elif(opcode=="nop"):
            nova[i][0]="jmp "+str(value)
            cont,loop=execute(nova)

            
            if(loop==1):
                return cont
    return -1

def main():
    inp=ReadInput("8.txt")

    print(TrialError(inp))

if __name__ == "__main__":
    main()