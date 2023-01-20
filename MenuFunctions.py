import csv  # Eric Salkovic
import pandas as pd


class MenuFunctions:
    """MenuFunctions class containing functions to print and execute commands in the menu"""
    def make_menu(self):
        """function to create and display menu to the user"""
        print("Menu Options:")
        print("1. Print out all data")
        print("2. Print out metadata")
        print("3. Print the first 20 lines")
        print("4. Exit")  # Eric Salkovic
        # menu options for the user to choose from and execute

    def print_data(self):
        """function to print out all the data from parsed .csv file"""
        try:
            with open("32100358.csv", "r") as file:
                csvreader = csv.reader(file)
                header = [next(csvreader)]
                print(header)
                # printing header at the top of the output
                for row in csvreader:  # Eric Salkovic
                    print(row)
                    # parsing .csv file (if found) and printing out each row
        except FileNotFoundError:
            print("invalid file name")  # Eric Salkovic
            # outputting error message if the .csv file is not found
        except:
            print("something went wrong...")
            # any other error will output this error message

    def print_metadata(self):
        """function to print out all metadata from parsed .csv file"""
        try:
            with open("32100358_MetaData.csv", "r") as file:
                csvreader = csv.reader(file)
                header = [next(csvreader)]
                print(header)
                # printing header at the top of the output
                for row in csvreader:
                    print(row)
                    # parsing .csv file (if found) and printing out each row
        except FileNotFoundError:
            print("invalid file name")
            # outputting error message if the .csv file is not found
        except:
            print("something went wrong...")
            # any other error will output this error message

    def print_20(self):
        """function to print out the first 20 rows from the parsed .csv file, using the panda library"""
        try:
            pd.set_option('display.max_columns', None)
            pd.options.display.width = None
            # setting panda options to format the output
            data = pd.read_csv("32100358.csv", nrows=20)
            # inputting data read from .csv into 'data' variable name to print out
            print(data)
            # outputting data read
        except FileNotFoundError:
            print("invalid file name")
            # outputting error message if the .csv file is not found
        except:
            print("something went wrong...")
            # any other error will output this error message
