from dictionary import *
hexList=[]
hex2List=[]
lower=[]
with open('data.txt', 'r') as file:         #Read each line of data.txt pulled from data.pcap and append to hex2List
    for line in file:
        hex2List.append(line)


for data in hex2List:
    hexList.append(data[data.index("08")+2:])  #Remove all the unneeded data (before 08)

for i in range(0,len(hexList)):             #Remove more un needed data in the lines
    hexList[i]=hexList[i].replace("\n","")
    hexList[i]=hexList[i].strip()
    hexList[i]=hexList[i][9:]

for i in hexList:                       #Replace all the 0s and the /s in order to read using the dictionary. Print needed to visually asses
    string=i.replace("00","")           #which characters are capped (has 02 before and after it)
    string=string.replace(" ","")
    print(string)
    if(len(string)==2):
     lower.append(py_dict[string])
#print(lower)
str=""
print(str.join(lower))            #Does not print the flag, you need to chane some characters to a capped character by looking at the printed output above (ex. - == _)
