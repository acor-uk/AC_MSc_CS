import getValue

def getInt(val_name, min = 0, max = 0):
    #print (f"{min},{max}") # Used in debugging when I was having issues with the min and max values, it was due to the if min != 0 test, when I needed to test a case where min was 0 and max was 5
    try:
        value = int(getValue.getValue(val_name))
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