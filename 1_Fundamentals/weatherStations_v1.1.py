""" This module is intended to process data files containing historic observations data from weather stations in the UK
"""
# import useful libraries
import os
import shutil as sh
# will import pandas and numpy later to verify the data

def writeToFile(data):
    try:
        dir = "processed"
        path = os.path.join(dir,"processedData.csv") #using join to handle the path separator
        file = open(path,"a") # open the file in append mode
    except FileNotFoundError:
        print("File Not Found: Create New File or Directory")
        os.mkdir(dir) # create the directory if it does not exist
        file = open(path,"w") # open the file in write mode the first time, so that it is created
        file.write("Station,Year,Month,Tmax,Tmin,Af, Rain, Sun\n") # write the header to the file
        writeToFile(data) #use recursion to call the function again now that the file exists

    for line in range(dataStart,dataEnd):
        #print(type(line))
        #had real issues here when I tried to parse line as an f-string, but there was different lengths of data in the rows
        #I was getting an index out of range error and it was because the first 7 or 8 rows were shorter than the rest, due to containing information about the station
        tempStr = f"{station},{data[line][0]},{data[line][1]},{data[line][2]},{data[line][3]},{data[line][4]},{data[line][5]},{data[line][6]}\n" #put the station name at the start of each line, but might change this to the long lat later
        file.write(tempStr) # I have to add the newline character when usinng the write method
    file.close()

def read_file(path):
    """ This function reads a file and returns the contents as a list of lines
    """
    try:
        file = open(path,"rt")
    except FileNotFoundError: # if the file does not exist, create it
        file = open(path,"w")
        file.close()
        return read_file()
    return file
# check for the data folder using relative path
# will need logic to handle if the folder does not exist and create it
files = os.listdir("data")

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
station = fileData[0][0]
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
dataStart = count
dataEnd = len(fileData)-1

if dataEnd - dataStart < 1:
    print("No Data Found")
    exit()
    
if fileData[dataEnd][0] == "Site":
    print("Site Now Closed")
    dataEnd -= 1

for row in range(dataStart,dataEnd):
    #print(row)
    for col in range(2,7):
        #print(row,col,str(fileData[row][col]+"\n"))
        try:
            tempStr = fileData[row][col]
        except IndexError:
            print(f"Index Error at {row},{col}") # some rows are shorter than others so need to handle this
            fileData[row].append("---") # add a placeholder value which can be easily ignored in calculations
        lastValue = len(tempStr)-1
        if(tempStr[-1]=="*"):
            #print(f"Found: {tempStr} at {row}")
            tempStr = tempStr[0:-1]
            fileData[row][col] = tempStr # remove the asterisk from the value if there is one
            #the last asterisk is not being removed, so need to check the length of the string

for row in range(count,len(fileData)):
    try:
        #cast to correct types
        #TODO need to handle the non-numeric values too
        fileData[row][0] = int(fileData[row][0]) # do I really need to cast the year to an int?
        fileData[row][1] = int(fileData[row][1]) # do I really need to cast the month to an int?
        #probably don't need to handle the above as int, it reduces complexity to leave as string

        #will probably make this a for loop to handle the invalid values
        """fileData[row][2] = float(fileData[row][2])
        fileData[row][3] = float(fileData[row][3])
        fileData[row][4] = float(fileData[row][4])
        fileData[row][5] = float(fileData[row][5])
        fileData[row][6] = float(fileData[row][6])
        """
        for col in range(2,7):
            if fileData[row][col] == "---":
                continue
            else:
                fileData[row][col] = float(fileData[row][col])

    except ValueError:
        print(f"Value Error at {row}")
        print(fileData[row])
        #cycle through the row and find the non-numeric value
        #TODO need to handle that the first exception will stop the casting of subsequent values
        for col in range(len(fileData[row])):
            value = fileData[row][col]
            if type(value) == str:
                index = fileData[row].index(value)
                #print(f"{value} in {index}")

writeToFile(fileData)