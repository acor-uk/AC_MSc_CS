"""tax calculator exercise"""

running = True

def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == ""):
        print("Value Cannot Be Empty")
        getValue()
    else:
        return value

def getNum(val_name):
    try:
        return int(getValue(val_name))
    except ValueError:
        print("Value Must Be a Number")
        getNum(getValue(val_name))

def open_file():
    try:
        file = open("taxes.csv","rt")
    except FileNotFoundError:
        file = open("taxes.csv","w")
        file.close()
        open_file()
    return file

tax_file = open_file()


headers = (tax_file.readline()).rstrip()
addresses = tax_file.readlines(0)

f_name = getValue("First Name")
s_name = getValue("Second Name")
dob_day = getNum("Date of Birth - Day")
dob_month = getNum("Date of Birth - Month")
dob_year = getNum("Date of Birth - Year")
gross_income = getNum("Gross Income")
dependent = getValue("Number of Dependents")