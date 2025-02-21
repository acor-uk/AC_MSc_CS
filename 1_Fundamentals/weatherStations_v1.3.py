import os
import matplotlib.pyplot as plt

headers = ""
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

lineColours = ["b","g","r","c","m","y","k","w"] #list of colours for the lines on the graph

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

#Get Value helps to get input from the user and validate for presence
def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == "" or value == " " or value == None):
        print("Value Cannot Be Empty")
    else:
        #print(value)
        return value
#Get Int uses getValue and then also validates for type int
def getInt(val_name, min = 0, max = 0):
    #print (f"{min},{max}") # Used in debugging when I was having issues with the min and max values, it was due to the if min != 0 test, when I needed to test a case where min was 0 and max was 5
    try:
        value = int(getValue(val_name))
        if(max > min): # removed the test to check if min wasn't 0
            if(value < min or value > max):
                print(f"Value Must Be Between {min} and {max}")
                return getInt(val_name, min, max)
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
        file.write("Station,Year,Month,Tmax (Celcius),Tmin (Celcius),Af, Rain (mm), Sun (hours)\n") # write the header to the file
        writeToFile(station, data, dataStart, dataEnd) #use recursion to call the function again now that the file exists
    except PermissionError:
        print("Permission Denied")
        exit()
    
    isFileEmpty = os.stat(path).st_size == 0 # check if the file is empty
    if isFileEmpty:
        file.write("Station,Year,Month,Tmax (Celcius),Tmin (Celcius),Af, Rain (mm), Sun (hours)\n")

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
        return read_file(path)
    return file

def selectFile():
    checkDirectory("data")
    files = os.listdir("data")

    for file in files:
        index = files.index(file)
        print(f"{index+1}: {file}")


    source = getInt("Select Source by Index: (Or 0 to Return to Main Menu)")
    if source == 0:
        #mainMenu() - This was causing issues as the function would continue running after the
        #mainMenu was called, so I replaced it with return
        return False

    try:
        targetFile = files[source-1]
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
    try:    
        stationNames.pop(0) # remove the headers from the data
    except IndexError:
        print("No Data Found")
        mainMenu()

    global headers
    headers = allStationData.pop(0) # the first index is from headers, so removing it, but saving for later

    stationSet = set(stationNames) #set creates a set, and so it removes all duplicates, essentially the same as a tuple

    count = 1
    stations = []
    for station in stationSet:
        print(f"{count}: {station}")
        stations.append(station) #temp list to be able to access the selected station later
        count+=1
    max = len(stations)
    print(f"{max} Stations Found")
    
    choice = getInt(f"Choose Station by Index (or 0 to Return to Main Menu)",0,len(stations))
    
    if choice == 0:
        return False

    selectedStation = stations[choice-1]
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
    if currentFile == False:
        return

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
            if(tempStr[-1]=="*" or tempStr[-1]=="#" or tempStr[-1]=="$"):
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

def selectMetric(headers):
    count = 0
    #print(headers)
    print("Select a Metric to Query:")
    for header in headers:
        #print(count,header)
        if count > 2:
            print(f"{count -2}:{header}")
        count += 1
    metric = getInt("Metric",1,count-3) # has to be less than 3 as the count goes up once more after the loop finishes
    return metric

def querySourceMenu():
    print("============= Query Station Menu ================\n")
    stationData = selectStation()
    if stationData == False:
        return
    selectedStation = stationData[0][0]
    #print(stationData) #used in dev / debug
    month = getInt("Enter Month as 1 - 12",1,12) # need to add range checking here / update the getInt function
    # took this part out as I might be reusing it later, so defined selectMetric function
    """
    count = 0
    print("Select a Metric to Query:")

    for header in headers:
        if count > 2:
            print(f"{count -2}:{header}")
        count += 1
    metric = getInt("Metric",1,count-2)
    selectedMetric = headers[metric+2]
    """
    
    metric = selectMetric(headers)
    selectedMetric = headers[metric+2]
    result = []
    invalidValueCount = 0 # some of the rows contain --- due to lack of data, which is not a valid value
    invalidValues = [] # list to store the invalid values, so can report on them if required
    rowCount = 0 # count the number of rows processed
    for row in stationData:
        if int(row[2])== month:
            rowCount += 1
            #print(f"{row[0]}-{row[1]}-{row[2]}: {row[metric+2]}")
            try:
                result.append([row[1],float(row[metric+2])])
            except ValueError:
                invalidValueCount += 1
                invalidValues.append(f"Invalid Value Found: {row[0]}-{row[1]}-{row[2]}")
                #print(f"Invalid Value Found: {row[0]}-{row[1]}-{row[2]}") # Used in Dev / Debug
    
    print(f"{invalidValueCount} Invalid Values Found in: {rowCount} Rows")
    input("Any Key Continue")
    clearConsole()
    max = float(result[0][1])
    min = float(result[0][1])
    total = 0
    xpoints = []
    ypoints = []
    print("%-10s%10s" % ("Year",selectedMetric)) # output as a two-col table
    for row in result:
        total += row[1]
        xpoints.append(row[0])
        ypoints.append(row[1])
        print("%-10s%10s" % (row[0],f"{row[1]:.1f}")) # output as a two-col table
        if row[1] > max:
            max = row[1]
        elif row[1] < min:
            min = row[1]
    #print(xpoints, ypoints) #Used in development and debugging
    sorted_ypoints = sorted(ypoints)
    median = ypoints[len(sorted_ypoints) // 2]
    total = sum(ypoints)
    mean = total / len(result)
    print(f"\nMax Value {selectedMetric}: {max}\n")
    print(f"Min Value {selectedMetric}: {min}\n")
    print(f"Average (Mean) {selectedMetric} for {selectedStation} in {months[month-1]} is: {mean:.2f}\n")
    print(f"Median Value {selectedMetric}: {median}\n")
    # The Standard Deviation can help me to see how spread out the values are, low standard deviation means the values are close to the mean.
    sq_deviations = []
    for row in ypoints:
        #print((row - mean)**2) # used in development and debugging
        sq_deviations.append((row - mean)**2) # initially I forgot to square the deviation
    standard_deviation = (sum(sq_deviations) / len(ypoints))** 0.5 # (Ozdemir, 2024) I also forgot to square root the sum of the squared deviations
    print(f"Standard Deviation: {standard_deviation:.2f}\n")
    input("Any Key to Continue")
    clearConsole()
   #print(result) #Used in development and debugging

    plt.figure(figsize=(8,9),num=f"Figure 1: {selectedMetric}") #How to change the figure size (Peipenbreier, N. 2022) & change the figure window title (Collins, E. 2024)
    plt.title(f"Historical {selectedStation} Station Values: {selectedMetric}")
    plt.axhline(y=median, color='r', linestyle='--', label=f'Median: {median}')
    plt.axhline(y=mean, color='g', linestyle='--', label=f'Mean: {mean}') #How to add a horizontal line to a graph (w3schools, 2025)
    plt.plot(xpoints, ypoints, marker = "o") #How to plot a graph with pyplot (w3schools, 2025)
    plt.xlabel("Year")
    plt.xticks(rotation = 90) #How to rotate the x-axis labels (Geeks for Geeks, 2022)
    plt.ylabel(headers[metric+2])
    plt.legend(loc="upper right") #How to add a legend to a graph (w3schools, 2025)
    plt.show()
    input("Any Key to Continue")
    plt.title("Figure 2. Histogram of "+selectedMetric)
    plt.ylabel("Frequency")
    plt.xlabel(selectedMetric)
    plt.axvline(median,color="r",linestyle="--",label=f'Median: {median}')
    plt.axvline(mean, color='g', linestyle='--', label=f'Mean: {mean}') 
    plt.hist(ypoints)
    plt.legend(loc="upper right") #How to add a legend to a graph (w3schools, 2025)
    plt.show()
    #input("Any Key to Continue") # Not really required as once the graph is closed, the programme will continue to main menu, or should it return to the query menu?
    querySourceMenu()

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
    choice = getInt("Option",0,3)
    """
    # replaced with getInt function as calling mainMenu again was causing an issue
    try:
        choice = int(choice)
    except Exception:
        print("Number must be an integer")
        mainMenu()
    #print("Integer Found")
    """
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