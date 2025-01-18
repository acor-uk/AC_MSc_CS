import sphere

def menu():
    print("Calculate New Sphere? (y/n)")
    response = input().strip().lower()
    if response == "n": # If the response is "n", break the loop
        return False
    print("Enter the sphere radius: ")
    radius = input().strip() # Get a value for Edge from user
    if radius == "" or radius == " " or not(radius): # If the value is empty, print an error message
        print("Value Cannot Be Empty")
    else:
        try:
            radius = float(radius)
        except ValueError: # If the value is not a number, print an error message
            print("Radius Must Be a Number")
        else:
            new_sphere = sphere.sphere(radius) # Create a new cube object with the given edge length
            global spheres
            spheres.append(new_sphere)
            print(new_sphere)

def main():
    running = True
    global spheres
    spheres = [] # Create an empty list to store cube objects
    try:
        while running == True:
            menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        running = False

if __name__ == "__main__":
    main()
