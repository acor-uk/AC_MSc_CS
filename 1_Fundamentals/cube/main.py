import cube

def main():
    cubes = [] # Create an empty list to store cube objects
    while True:
        print("Calculate New Cube? (y/n)")
        response = input().strip().lower()
        if response == "n": # If the response is "n", break the loop
            break
        print("Enter the length of the cube edge: ")
        length = input().strip() # Get a value for Edge from user
        if length == "" or length == " " or not(length): # If the value is empty, print an error message
            print("Value Cannot Be Empty")
        else:
            try:
                length = float(length)
            except ValueError: # If the value is not a number, print an error message
                print("Value Must Be a Number")
            finally:
                new_cube = cube.cube(length)
                cubes.append(new_cube)
                print(new_cube)

if __name__ == "__main__":
    main()