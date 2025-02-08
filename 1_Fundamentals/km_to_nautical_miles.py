def get_value():
    try:
        km  = float(input("Enter distance in kilometers: "))
        return km
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_value()

km = get_value()
print(hex(id(km)))
MINUTES_PER_ARC = 60
MINUTES_PER_90 = 90 * MINUTES_PER_ARC
KM_PER_90 = 1/10000
nautical_miles = km * (KM_PER_90 * MINUTES_PER_90) #should be 0.5399568034557235 rounded up to .54
print(f"{km} kilometers is equal to {nautical_miles} nautical miles.")