def isListOfInts(l,n):
    if(type(l) is not list):
        raise ValueError(str(l) + " - arguments not of <list> type")
    else:
        if n==0:
            return True
        else:
            for i in range(0,n):
                if type(i) is int :
                    return True
                else:
                    return False
def testList(l,n):
    print(isListOfInts(l,n))
l=[]
n=int(input('enter the length of list'))
for i in range(0,n):
    m=input('enter the element to list')
    l.append(m)
testList(l,n)