import csv  # Eric Salkovic
import pandas as pd
from csv import DictReader


class MenuFunctions:
    """MenuFunctions class containing functions to print and execute commands in the menu"""

    def make_menu(self):
        """function to create and display menu to the user"""
        print("Menu Options:")
        print("1. Print out all data")
        print("2. Print out metadata")
        print("3. Print the first 20 lines")
        print("4. Exit")
        print("5. Reload dataset")
        print("6. Persist data to a new .csv file")
        print("7. Display single or multiple records")
        print("8. Create new record in .csv file")
        print("9. Edit record in .csv file")
        print("10. Delete record in .csv file")
        print("11. Sort .csv data in a data structure")
        print("Program by Eric Salkovic | 040861953")
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
            # outputting generic error message for other exceptions

    def reload_dataset(self):  # Eric Salkovic
        """function to reload and print the data in .csv file"""
        data = pd.read_csv("32100358.csv")
        # reading data in .csv file
        for index, row in data.iterrows():
            print(row['REF_DATE'], row['GEO'], row['DGUID'], row['Area, production and farm value of potatoes'],
                  row['UOM'], row['UOM_ID'], row['SCALAR_FACTOR'], row['SCALAR_ID'], row['VECTOR'], row['COORDINATE'],
                  row['VALUE'], row['STATUS'], row['SYMBOL'], row['TERMINATED'], row['DECIMALS'], )
        # looping through each row and printing data in .csv file by column

    def persist_new(self):
        """function to persist data to a new .csv file"""
        data = pd.read_csv("32100358.csv")
        # reading data in .csv file
        file = input("Name of new file: ")
        # getting name for new file to persist data to
        data.to_csv(file + ".csv", index=False)
        # sending read data to new file
        print("data successfully saved to new file")
        # printing success message

    def print_single_multiple(self):  # Eric Salkovic
        """function to print a single or multiple lines"""
        data = pd.read_csv("32100358.csv")
        # reading data in .csv file
        printnum = input("Would you like to print one or more rows? (one/more) ")
        # prompting user for printing one or more rows
        match str(printnum):
            # match/case decision structure to print one or more rows
            case "one":
                # case to print one row
                row = input("Which row would you like to print? ")
                # promting user to print row 'x'
                print(data.loc[int(row)])
                # printing selected row
            case "more":
                # case to print multiple rows
                rows = int(input("From which row would you like to start printing? "))
                # promting user to print starting from row 'x'...
                rows2 = int(input("To which row? "))
                # ...to row 'y'
                print(data[int(rows):int(rows2 + 1)])
                # printing selected rows
            case _:
                print("invalid input")
                # error message in case user enters wrong value

    def create_entry(self):
        """function to create and insert entry into given .csv file"""
        csvData = pd.read_csv("32100358.csv")
        # reading data in .csv file
        ref_date = input("REF_DATE: ")
        geo = input("GEO: ")
        dguid = input("DGUID: ")
        area = input("Area, production and farm value of potatoes: ")
        uom = input("UOM: ")
        uom_id = input("UOM_ID: ")
        scalar_factor = input("SCALAR FACTOR: ")
        scalar_id = input("SCALAR ID: ")
        vector = input("VECTOR: ")
        coord = input("COORDINATE: ")
        value = input("VALUE: ")
        status = input("STATUS: ")
        symbol = input("SYMBOL: ")
        term = input("TERMINATED: ")
        dec = input("DECIMAL: ")
        # gathering data for each column

        data = {
            'REF_DATE': [ref_date],
            'GEO': [geo],
            'DGUID': [dguid],
            'Area, Production and farm value of potatoes': [area],
            'UOM': [uom],
            'UOM_ID': [uom_id],
            'SCALAR_FACTOR': [scalar_factor],
            'SCALAR_ID': [scalar_id],
            'VECTOR': [vector],
            'COORDINATE': [coord],
            'VALUE': [value],
            'STATUS': [status],
            'SYMBOL': [symbol],
            'TERMINATED': [term],
            'DECIMALS': [dec]
        }
        # creating data dictionary to use as dataframe
        dataFrame = pd.DataFrame(data)
        # creating dataframe from user-entered data
        dataFrame.to_csv('32100358.csv', mode='a', index=False, header=False)
        # writing dataframe to .csv file
        print(csvData)
        # printing out new data from .csv file
        print("Data successfully appended")
        # printing success message

    def edit_entry(self):  # Eric Salkovic
        """function to edit a row in .csv file"""
        try:
            # try/except in case of failure
            data = pd.read_csv("32100358.csv")
            # reading data in .csv file
            print(data)
            # printing data to see which row user wants to edit
            row = input("What row would you like to edit? ")
            # promting user for which row number to edit
            col = input("What column would you like to edit? ")
            # promting user for which column name to edit
            newData = input("What is the new data you would like to add? ")
            # promting user for the updated data
            data.at[int(row), col] = newData
            # executing data edit in .csv file
            data.to_csv("32100358.csv", index=False)
            # writing edited data back to .csv file
            print(data)
            # reprinting data to view edit
            print("Data succesfully edited")
            # printing success message
        except:
            # exception handling
            print("something went wrong...")
            # printing out error message in case of exception

    def delete_entry(self):  # Eric Salkovic
        """funtion to delete a single row in .csv file"""
        try:
            data = pd.read_csv("32100358.csv")
            # reading data from .csv file
            print(data)
            # printing data to see the first and last 5 rows (to easily see newly added rows)
            row = input("What row # would you like to delete? ")
            # promting user for which row to delete
            data = data.drop(data.index[int(row)])
            # executing delete/drop row in .csv file
            data.to_csv("32100358.csv", index=False)
            # writing the data back to .csv file
            print(data)
            # reprinting data with updated data (delete/drop)
            print("Data successfully deleted")
            # printing success message
        except IndexError:
            # indexerror exception if row does not exist
            print("Row does not exist in .csv file")
            # printing appropriate error message for exception
        except:
            print("something went wrong...")
            # printing generic error message

    def print_name(self):
        """function for printing my name to prove this is my original work"""
        name = "Eric Salkovic"
        # variable holding my name
        studentnum = "040861953"
        # variable holding my student number
        print("Program by " + name + " | " + studentnum)
        # printing my name and student number

    def sort_dict(self):
        with open("32100358.csv", 'r') as data:
            dict_reader = DictReader(data)
            dict_list = list(dict_reader)

            for row in dict_list:
                print(f"REF_DATE: {row['REF_DATE']}, GEO: {row['GEO']}, DGUID: {row['DGUID']}, Area & Production &"
                      f" farm value of potatoes: {row['Area_production_and_farm_value_of_potatoes']}, UOM: {row['UOM']},"
                      f" UOMID: {row['UOM_ID']}, SCALAR FACTOR: {row['SCALAR_FACTOR']}, SCALAR ID: {row['SCALAR_ID']},"
                      f" VECTOR: {row['VECTOR']}, COORDINATE: {row['COORDINATE']}, VALUE {row['VALUE']}, STATUS: "
                      f"{row['STATUS']}, SYMBOL: {row['SYMBOL']}, TERMINATED: {row['TERMINATED']}, DECIMALS: {row['DECIMALS']}")
