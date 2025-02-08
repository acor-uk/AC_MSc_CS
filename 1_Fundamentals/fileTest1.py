""" This module is intended to process data files containing historic observations data from weather stations in the UK
"""

import os
import shutil as sh

def read_file(path):
    try:
        file = open(path,"rt")
    except FileNotFoundError:
        file = open(path,"w")
        file.close()
        return read_file()
    return file

files = os.listdir("data/")

for file in files:
    index = files.index(file)
    print(f"{index}: {file}")



source = int(input("Select Source by Index: "))
try:
    targetFile = files[source]
    currentFile = read_file(f"data/{targetFile}")
except IndexError:
    print("Invalid Index")
    exit()

fileData = []

for line in currentFile:
    temp = []
    temp = line.rsplit()
    #print(temp)
    fileData.append(temp)

#print(len(fileData))

headerFound = False
count=0
while headerFound == False:
    #print({fileData[count][0]})
    if(fileData[count][0] == "yyyy"):
        headers = fileData[count]
        headerFound = True
    else:
        count +=1
dataFound = False
while dataFound == False:
    try:
        int(fileData[count][0])
        dataFound = True
    except ValueError:
        count +=1

print(fileData[count])
print(count)
print(headers)
print(f"Data Rows: {len(fileData)-count}")

for row in range(count,len(fileData)):
    #print(row)
    for col in range(2,7):
        #print(row,col,str(fileData[row][col]+"\n"))
        try:
            tempStr = fileData[row][col]
        except IndexError:
            print(f"Index Error at {row},{col}") # some rows are shorter than others so need to handle this
            fileData[row].append("---") # add a placeholder value which can be easily ignored in calculations
        lastValue = len(tempStr)-1
        if(tempStr[lastValue]=="*"):
            #print(f"Found: {tempStr} at {row}")
            tempStr = tempStr[0:lastValue]
            fileData[row][col] = tempStr # remove the asterisk from the value if there is one

for row in range(count,len(fileData)):
    try:
        #cast to correct types
        #TODO need to handle the non-numeric values too
        fileData[row][0] = int(fileData[row][0])
        fileData[row][1] = int(fileData[row][1])
        fileData[row][2] = float(fileData[row][2])
        fileData[row][3] = float(fileData[row][3])
        fileData[row][4] = float(fileData[row][4])
        fileData[row][5] = float(fileData[row][5])
        fileData[row][6] = float(fileData[row][6])
    except ValueError:
        print(f"Value Error at {row}")
        print(fileData[row])
        #cycle through the row and find the non-numeric value
        #TODO need to handle that the first exception will stop the casting of subsequent values
        for col in range(len(fileData[row])):
            value = fileData[row][col]
            if type(value) == str:
                index = fileData[row].index(value)
                print(f"{value} in {index}")
