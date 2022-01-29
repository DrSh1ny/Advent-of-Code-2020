def Search(lista,elem):
    for i in range(len(lista)-2,-1,-1):
        if(lista[i]==elem):
            return i
    return -1

def Search1(lista,elem):
    for i in range(len(lista)-1,-1,-1):
        if(lista[i][0]==elem):
            return lista[i]
    return -1

def main():
    inp=[9,3,1,0,8,4]
    """
    for i in range(50):
        valor=Search(inp,inp[-1])
        if(valor==-1):
            inp.append(0)
        else:
            inp.append(len(inp)-1-valor)
    print(inp)
    print(inp[-1])

    """
    dic={9:0,3:1,1:2,0:3,8:4}
    
    for i in range(29999994):
        #print(dic)
        #print(inp)
        valor=inp[-1]
        try:
            age=len(inp)-1-dic[valor]
            inp.append(age)
            dic[valor]=i+5
        except:
            inp.append(0)
            dic[valor]=i+5
            
    
    #print(appear)
    #print(inp)
    print(inp[-1])
    
    
if __name__ == "__main__":
    main()