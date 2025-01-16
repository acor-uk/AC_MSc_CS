#AddressBook

running = True

def open_file():
    try:
        file = open("addresses.csv","rt")
    except FileNotFoundError:
        file = open("addresses.csv","w")
        file.close()
        return open_file()
    return file

address_file = open_file()


headers = (address_file.readline()).rstrip()
addresses = address_file.readlines(0)

address_book = {}

for line in addresses:
    #print(line.rstrip())
    stripped = line.rstrip()
    if(stripped == headers):
        #print(True)
        continue
    else:
        components = line.split(",")
        address = {"Building":components[1],"Street":components[2],"Town":components[3],"Post code": components[4],"Phone":components[5]}
        address_book[components[0]] = address

#print(address_book)
def print_contacts():
    print("===================== CONTACTS =======================")
    for address in address_book:
        print("------------------------------------------------")
        name = address
        print(f"Name: {address}")
        keys = address_book[address].keys()
        for key in keys:
                print(f"{key}: {address_book[address][key]}")

def list_contacts():
    print("===================== CONTACTS =======================")
    for address in address_book:
        print("------------------------------------------------")
        name = address
        print(f"Contact: {address}")

def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == ""):
        print("Value Cannot Be Empty")
        getValue()
    else:
        return value

def store_contact(name,address):
    #still need to implement saving back to the file
    address_file = open("addresses.csv","a")
    print(f"Storing contact {name} ...")
    address_file.write("\n")
    address_file.write(f"name,")
    count = 0
    numKeys = len(address)
    for key in address:
        if(count == numKeys - 1):
            address_file.write(f"{address[key]}")
        else:
            address_file.write(f"{address[key]},")
        count += 1
    address_file.close()

def new_contact():
    name = getValue("Name")
    bulding = getValue("Building (Name or Number)")
    street = getValue("Street")
    town = getValue("Town")
    post_code = getValue("Post Code")
    phone = getValue("Phone Number")

    address = {"Building":bulding,"Street":street,"Town":town,"Post code": post_code,"Phone":phone}

    address_book[name] = address
    store_contact(name,address)

def show_contact():
    list_contacts()
    selection = input("Enter the name of the contact you want to view: ")
    if selection in address_book:
        print(f"Contact: {selection}")
        keys = address_book[selection].keys()
        for key in keys:
            print(f"{key}: {address_book[selection][key]}")
    else:
        print("Contact not found.")

def main_menu():
    global running
    print("=========== Address Book =================")
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. Show Contact")
    print("3. Show All Contacts")
    print("4. Exit")
    print("Choose an option:")
    selection = ""
    try:
        selection = int(input())
    except ValueError:
        print("Selection must be an integer.")
        main_menu()

    match(selection):

        case 1:
            new_contact()
        case 2:
            show_contact()
        case 3:
            print_contacts()
        case 4:
            print("Exiting...")
            running = False



try:
    while running == True:
        main_menu()
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
    running = False