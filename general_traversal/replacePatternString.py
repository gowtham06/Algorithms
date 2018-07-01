def checkForPattern(string, startIndex,sourcePattern):
    counter=startIndex
    boolVal=True
    for item in sourcePattern:
        if(item!=string[counter]):
            boolVal=False
            break
        counter+=1
    return boolVal
def replacePattern(str,indexList,sourceList,targetList):
    temp_str=str
    for index,item in enumerate(indexList):
        startCounter = len(str) - len(temp_str) + indexList[index]
        boolVal=checkForPattern(str,startCounter,sourceList[index])
        if(boolVal==True):
            # startCounter=len(str)-len(temp_str)+indexList[index]
            print(indexList[index],startCounter)
            str=list(str)
            print(str)
            counter=0
            # replaceCounter=0
            replaceList=[]
            while(counter<len(sourceList[index])):
                str[startCounter]=chr(startCounter)
                replaceList.append(chr(startCounter))
                startCounter+=1
                counter+=1
            str=''.join(str)
            # print(str,targetList[index])
            str=str.replace(''.join(replaceList),targetList[index])
            print(str)

if __name__ == '__main__':
    str="abcd"
    indexList=[0,2]
    sourceList=["ab","ec"]
    targetList=["eee","ffff"]
    replacePattern(str,indexList,sourceList,targetList)