import csv
from Potatoes import Potatoes
from pprint import pprint

try:
    with open("32100358.csv", "r") as file:
        csvreader = csv.reader(file)
        header = [next(csvreader)]
        for row in csvreader:
            print(row)
    potato1 = Potatoes(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                       row[7], row[8], row[9], row[10], row[11], row[12], row[13])
except FileNotFoundError:
    print("invalid file name")
except:
    print("something went wrong...")

print(str(potato1))