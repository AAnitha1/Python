def isWhiteLine(line):
    if line =='\n':
        return True
    else:
        return False
    
import fileinput
f=fileinput.input()
f1=open("output.txt", "w+")
for line in f:
    print(line)
    if isWhiteLine(line)!= True:
        f1.writelines(line)