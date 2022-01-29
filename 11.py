import copy
def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        linha=linha.strip("\n").strip(" ")
        linha=list(linha)
        a.append(linha)
        linha=f.readline()
    return a

def PrintMatrix(matrix):
    print("\n")
    for i in matrix:
        print(i)

def State(matrix,posX,posY,ofsetX,ofsetY):
    
    if(ofsetX==0 and ofsetY==0):
        return 0
    if(posX+ofsetX>=len(matrix[0]) or posX+ofsetX<0):
        return 0
    if(posY+ofsetY>=len(matrix) or posY+ofsetY<0):
        return 0
    if(matrix[posY+ofsetY][posX+ofsetX]=="."):
        return 0

    if(matrix[posY+ofsetY][posX+ofsetX]=="L"):
        return 0
    if(matrix[posY+ofsetY][posX+ofsetX]=="#"):
        return 1
    
def State1(matrix,posX,posY,ofsetX,ofsetY):
    if(ofsetX==0 and ofsetY==0):
        return 0
    
    posX+=ofsetX
    posY+=ofsetY
    while(posX<len(matrix[0]) and posY<len(matrix) and posX>=0 and posY>=0 and matrix[posY][posX]=="."):
        posX+=ofsetX
        posY+=ofsetY
    
    if(posX>=len(matrix[0]) or posY>=len(matrix) or posX<0 or posY<0):
        return 0
    if(matrix[posY][posX]=="L"):
        return 0
    if(matrix[posY][posX]=="#"):
        return 1
    return 0
        
def ChangeState(matrix):
    nova=copy.deepcopy(matrix)
    smthchgnd=0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            counter=0
            for i in range(-1,2):
                for j in range(-1,2):
                    counter+=State(matrix,x,y,i,j)
            
            if(matrix[y][x]=="L" and counter==0):
                nova[y][x]="#"
                smthchgnd=1
            if(matrix[y][x]=="#" and counter>3):
                nova[y][x]="L"
                smthchgnd=1
    
    matrix=nova
    return matrix,smthchgnd

def ChangeState1(matrix):
    nova=copy.deepcopy(matrix)
    smthchgnd=0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            counter=0
            for i in range(-1,2):
                for j in range(-1,2):
                    counter+=State1(matrix,x,y,i,j)
            
            if(matrix[y][x]=="L" and counter==0):
                nova[y][x]="#"
                smthchgnd=1
            if(matrix[y][x]=="#" and counter>4):
                nova[y][x]="L"
                smthchgnd=1
    
    matrix=nova
    return matrix,smthchgnd

def CountOcupied(matrix):
    counter=0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(matrix[y][x]=="#"):
                counter+=1
    return counter

def main():
    inp=ReadInput("11.txt")
    
    #PrintMatrix(inp)
    inp,inutil=ChangeState1(inp)
    while(inutil!=0):
        inp,inutil=ChangeState1(inp)
        
    #PrintMatrix(inp)
    print(CountOcupied(inp))
    

    
if __name__ == "__main__":
    main()