import os
import matplotlib.pyplot as plt

headers = ""

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

#Get Value helps to get input from the user and validate for presence
def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == "" or value == " " or value == None):
        print("Value Cannot Be Empty")
    else:
        print(value)
        return value
#Get Int uses getValue and then also validates for type int
def getInt(val_name):
    try:
        value = int(getValue(val_name))
        return value
    except ValueError:
        print("Value Must Be a Number")
        return getInt(val_name)
    except TypeError: #had a lot of problems here, when putting a valid input in, after an invalid input
        print("Value Must Be a Number")
        return getInt(val_name)

def checkDirectory(name):
    # check that a directory exists
    if not(os.path.isdir(name)):
        #if the directory doesn't exist, output message and create the directory
        print(f"{name} Directory Not Found!")
        try:
            os.mkdir(name)
            print(f"Directory {name} Successfully Created.")
        except FileNotFoundError as e:
            print(f"Error creating directory {name}: {e}")
        except PermissionError as e:
            print(f"Permission denied: {e}")
        except OSError as e:
            print(f"OS error: {e}")
    else:
        print(f"Directory: '{name}' Found.")

def writeToFile(station, data, dataStart, dataEnd):
    try:
        dir = "processed"
        path = os.path.join(dir,"processedData.csv") #using join to handle the path separator
        file = open(path,"a") # open the file in append mode
    except FileNotFoundError:
        print("File Not Found: Create New File or Directory")
        os.mkdir(dir) # create the directory if it does not exist
        file = open(path,"w") # open the file in write mode the first time, so that it is created
        file.write("Station,Year,Month,Tmax,Tmin,Af, Rain, Sun\n") # write the header to the file
        writeToFile(station, data, dataStart, dataEnd) #use recursion to call the function again now that the file exists

    for line in range(dataStart,dataEnd):
        #print(type(line))
        tempStr = f"{station},{data[line][0]},{data[line][1]},{data[line][2]},{data[line][3]},{data[line][4]},{data[line][5]},{data[line][6]}\n" #put the station name at the start of each line, but might change this to the long lat later
        print(tempStr)
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

def selectFile():
    checkDirectory("data")
    files = os.listdir("data")

    for file in files:
        index = files.index(file)
        print(f"{index}: {file}")


    source = getInt("Select Source by Index: ")
    try:
        targetFile = files[source]
        currentFile = read_file(f"data/{targetFile}")
    except IndexError:
        print("Invalid Index")
        addSourceMenu()
    except ValueError:
        print("Invalid Index")
        addSourceMenu()
    return currentFile

def getProcessedData():
    checkDirectory("processed") #if the directory doesn't exist, it is created
    dir = "processed"
    path = os.path.join(dir,"processedData.csv") #using join to handle the path separator
    file = read_file(path)
    return file

def selectStation():
    file = getProcessedData()
    stationNames = []
    allStationData = []
    
    for line in file:
        line = line.strip()
        allStationData.append(line.split(","))
        stationNames.append(line.split(",")[0])
    stationNames.pop(0) # remove the headers from the data
    global headers
    headers = allStationData.pop(0) # the first index is from headers, so removing it, but saving for later

    stationSet = set(stationNames) #set creates a set, and so it removes all duplicates, essentially the same as a tuple

    count = 1
    stations = []
    for station in stationSet:
        print(f"{count}: {station}")
        stations.append(station)
        count+=1

    selectedStation = stations[getInt("Station")-1]
    print(selectedStation)
    
    result = []
    for row in allStationData:
        if row[0] == selectedStation:
            result.append(row)

    return result

def addSourceMenu():
    print("============= Add Station Menu ================\n")
    # check for the data folder using relative path
# will need logic to handle if the folder does not exist and create it
    currentFile = selectFile()

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

    writeToFile(station,fileData,dataStart,dataEnd)

def querySourceMenu():
    print("============= Query Station Menu ================\n")
    stationData = selectStation()
    print(stationData)
    month = getInt("Enter Month as 1 - 12")
    count = 0
    print("Select a Metric to Query:")
    for header in headers:
        if count > 2:
            print(f"{count -2}:{header}")
        count += 1
    metric = getInt("Metric")
    result = []
    
    for row in stationData:
        if int(row[2])== month:
            #print(f"{row[0]}-{row[1]}-{row[2]}: {row[metric+2]}")
            try:
                result.append([row[1],float(row[metric+2])])
            except ValueError:
                print(f"Invalid Value Found: {row[0]}-{row[1]}-{row[2]}")
    
    max = float(result[0][1])
    min = float(result[0][1])
    total = 0
    xpoints = []
    ypoints = []
    
    for row in result:
        total += row[1]
        xpoints.append(row[0])
        ypoints.append(row[1])
        if row[1] > max:
            max = row[1]
        elif row[1] < min:
            min = row[1]
    print(xpoints, ypoints)
    print(f"Max Value: {max}")
    print(f"Min Value: {min}")
    print(f"Average for {stationData[0][0]} in {month} is: {total/len(result)}")
    input("Enter to Continue")
    print(result)
    input("")
    

    plt.plot(xpoints, ypoints, marker = "o")
    plt.xlabel("Year")
    plt.ylabel(headers[metric+2])
    plt.show()
    input("")
    

    
def queryAllStations():
    print("============= Querying All Stations ================\n")

def mainMenu():
    clearConsole()
    print("""============= Main Menu ================\n
    Choose an Option:\n
    0. Exit
    1. Add New Station
    2. Query Station
    3. Query All Stations
          """)
    choice = input()
    try:
        choice = int(choice)
    except Exception:
        print("Number must be an integer")
        mainMenu()
    #print("Integer Found")
    match(choice):
        case 0:
                print("Programme Closing...")
                exit()
        case 1:
            addSourceMenu()
        case 2:
            querySourceMenu()
        case 3:
            queryAllStations()

#FIRST RUN...
#Check the data and processed directories exist
checkDirectory("data")

#set running to True
running = True

#Main Loop with an exception for keyboard interrupt CTRL + C
try:
    while running == True:
        mainMenu()
except KeyboardInterrupt:
    print("""
          Keyboard Interrupt Detected
          Programme Closing...
          """)