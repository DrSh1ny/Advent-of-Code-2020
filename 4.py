import re

def ReadInput(ficheiro):
    f=open(ficheiro,"r")
    a=[]
    
    linha=f.readline()
    while(linha):
        passport=""
        while(linha!='\n' and linha):
            passport+=" "+linha.strip("\n")
            linha=f.readline()

        a.append(passport)
        linha=f.readline()
        
    f.close()
    return a

def CuratePassport(passport):
    tags=[]
    pairs=[]
    
    passport=passport.strip()
    pieces=passport.split(" ")
    for i in pieces:
        i=i.split(":")
        tags.append(i[0])
        pairs.append(i)

    return tags,pairs

def CuratePair(pair):
    key=pair[0]
    value=pair[1]
    print(key)
    print(value)
    if(key=="byr"):
        pattern="[0-9][0-9][0-9][0-9]"
        result = re.fullmatch(pattern, value)
        if(result==None or int(value)<1920 or int(value)>2002):
            return 0
        else:
            return 1

    elif(key=="iyr"):
        pattern="[0-9][0-9][0-9][0-9]"
        result = re.fullmatch(pattern, value)
        if(result==None or int(value)<2010 or int(value)>2020):
            return 0
        else:
            return 1
    
    elif(key=="eyr"):
        pattern="[0-9][0-9][0-9][0-9]"
        result = re.fullmatch(pattern, value)
        if(result==None or int(value)<2020 or int(value)>2030):
            return 0
        else:
            return 1
    
    elif(key=="hgt"):
        pattern="[0-9]+cm"
        result = re.fullmatch(pattern, value)
        if(result!=None and int(value[0:-2])>=150 and int(value[0:-2])<=193):
            return 1
        pattern="[0-9]+in"
        result = re.fullmatch(pattern, value)
        if(result!=None and int(value[0:-2])>=59 and int(value[0:-2])<=76):
            return 1
        return 0

    elif(key=="hcl"):
        pattern="#([0-9a-f]{6,6})"
        result = re.fullmatch(pattern, value)
        if(result==None):
            return 0
        else:
            return 1

    elif(key=="ecl"):
        pattern="(amb|blu|brn|gry|grn|hzl|oth)"
        result = re.fullmatch(pattern, value)
        if(result==None):
            return 0
        else:
            return 1
    
    elif(key=="pid"):
        pattern="[0-9]{9,9}"
        result = re.fullmatch(pattern, value)
        if(result==None):
            return 0
        else:
            return 1

    elif(key=="cid"):
        return 1

    return 0



    

def main():
    inp=ReadInput("4.txt")
    acronyns=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    acronyns.sort()
    acronyns1=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    acronyns1.sort()

    count=0
    for i in inp:
        tags,pairs=CuratePassport(i)
        tags.sort()
        if(tags!=acronyns and tags!=acronyns1):
            continue
        total=1
        for i in pairs:
            result=CuratePair(i)
            print(result)
            if(result==0):
                total=0
        if(total==1):
            count+=1
                
    print(count)
    





if __name__ == "__main__":
    main()