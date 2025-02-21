def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == "" or value == " " or value == None):
        print("Value Cannot Be Empty")
    else:
        #print(value)
        return value