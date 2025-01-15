import csv

with open('addresses.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0]) 