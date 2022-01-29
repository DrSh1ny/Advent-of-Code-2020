def CheckRule(minCount,maxCount,letter,password):
    password=list(password)
    num=password.count(letter)
    if(num<=maxCount and num>=minCount):
        return 1
    else:
        return 0

def CheckRule1(index1,index2,letter,password):
    password=list(password)
    check=0
    if(password[index1-1]==letter):
        check+=1
    if(password[index2-1]==letter):
        check+=1
    if(check==1):
        print("{} {} {} {}".format(index1,index2,letter,password))
        return 1
    else:
        return 0

def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        a.append(linha)
        linha=f.readline()
    f.close()
    return a


def main():
    countCorrect=0
    inp=ReadInput("2.txt")
    for linha in inp:
        linha=linha.split()
        aux=linha[0]
        letter=linha[1][0]
        password=linha[2]

        aux=aux.split("-")
        minC=int(aux[0])
        maxC=int(aux[1])

        if(CheckRule1(minC,maxC,letter,password)==1):
            countCorrect+=1

    print(countCorrect)

if __name__ == "__main__":
    main()