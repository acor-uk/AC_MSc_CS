"""tax calculator exercise"""

running = True

#Get Value helps to get input from the user and validate for presence
def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == ""):
        print("Value Cannot Be Empty")
        getValue()
    else:
        return value
#Get Int uses getValue and then also validates for type int
def getInt(val_name):
    try:
        return int(getValue(val_name))
    except ValueError:
        print("Value Must Be a Number")
        return getInt(getValue(val_name))

#Get Float uses getValue and then also validates for type float
def getFloat(val_name):
    try:
        return float(getValue(val_name))
    except ValueError:
        print("Value Must Be a Number")
        return getFloat(getValue(val_name))

#Open file checks if the file exists and if not creates it
def open_file():
    try:
        file = open("taxes.csv","rt")
    except FileNotFoundError:
        file = open("taxes.csv","w")
        file.close()
        return open_file()
    return file

#Save file writes the new tax payer to the file
def save_file():
    tax_file = open("taxes.csv","a")
    tax_file.write(f"{f_name},{s_name},{dob_day},{dob_month},{dob_year},{gross_income},{dependents},{tax},{net_income}\n")
    tax_file.close()

#Main Program

tax_file = open_file()
running = True
headers = tax_file.readline().rstrip()
tax_payers = tax_file.readlines(0)
while running:
    print("Do you want to add a new tax payer? (y/n)")
    response = input()
    if response == "n":
        running = False
    else:
        f_name = getValue("First Name")
        s_name = getValue("Second Name")
        dob_day = getInt("Date of Birth - Day")
        dob_month = getInt("Date of Birth - Month")
        dob_year = getInt("Date of Birth - Year")
        gross_income = getFloat("Gross Income")
        dependents = getInt("Number of Dependents")
        deductable_income = 10000 + (dependents * 3000)
        taxable_income = gross_income - (deductable_income)
        tax =  round((taxable_income) * 0.2,2)
        tax_f = format(tax, '.2f')
        net_income = format(gross_income - tax, '.2f')

        print(f"Name: {s_name}, {f_name}. DOB: {dob_day}/{dob_month}/{dob_year}. Gross Income: {gross_income}. Tax: {tax_f}. Net Income: {net_income}")

        save_file()