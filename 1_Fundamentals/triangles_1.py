def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == ""):
        print("Value Cannot Be Empty")
        getValue()
    else:
        return value

#Get Float uses getValue and then also validates for type float
def getFloat(val_name):
    try:
        return float(getValue(val_name))
    except ValueError:
        print("Value Must Be a Number")
        return getFloat(getValue(val_name))

running = True
#Main
def main():

    inputA = getFloat(" Please Enter the Value for side A")
    inputB = getFloat(" Please Enter the Value for side B")
    inputC = getFloat(" Please Enter the Value for side C")

    if (inputA == inputB == inputC):
        print("The Triangle is Equilateral")
    elif (inputA == inputB or inputB == inputC or inputA == inputC):
        print("The Triangle is Isosceles")
    else:
        print("The Triangle is Scalene")
    
    if(inputA**2 == (inputB**2 + inputC**2) or inputB**2 == (inputA**2 + inputC**2) or inputC**2 == (inputA**2 + inputB**2)):
        print("The Triangle is a Right Angled Triangle")

try:
    while running == True:
        main()
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
    running = False