while True:
    print("Calculate New Cube? (y/n)")
    response = input().strip().lower() # Get a response from user
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
            face_area = length * length
            surface_area = 6 * face_area
            volume = face_area * length
            print(f"CUBE VALUES:\nFace Area: {face_area}\nSurface Area: {surface_area}\nVolume: {volume}")