import csv
from Potatoes import Potatoes

try:
    with open("32100358.csv", "r") as file:
        csvreader = csv.reader(file)
        header = [next(csvreader)]
        for row in csvreader:
            print(row)
    potato1 = Potatoes([0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13])
except FileNotFoundError:
    print("invalid file name")
except:
    print("something went wrong...")

print("potato1: " + str(potato1))
