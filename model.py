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
        print("11. Read/Print .csv data to a data dictionary")
        print("12. Add new record to data dictionary")
        print("13. Edit existing record in data dictionary")
        print("14. Delete existing record in data dictionary")
        print("15. Sort print multiple columns")
        print("Program by Eric Salkovic | 040861953")
        # menu options for the user to choose from and execute

    def print_data(self):
        """function to print out all the data from parsed .csv file"""
        try:
            with open("dataset.csv", "r") as file:
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
            with open("dataset_MetaData.csv", "r") as file:
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
            data = pd.read_csv("dataset.csv", nrows=20)
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
        data = pd.read_csv("dataset.csv")
        # reading data in .csv file
        for index, row in data.iterrows():
            print(row['REF_DATE'], row['GEO'], row['DGUID'], row['Area, production and farm value of potatoes'],
                  row['UOM'], row['UOM_ID'], row['SCALAR_FACTOR'], row['SCALAR_ID'], row['VECTOR'], row['COORDINATE'],
                  row['VALUE'], row['STATUS'], row['SYMBOL'], row['TERMINATED'], row['DECIMALS'], )
        # looping through each row and printing data in .csv file by column

    def persist_new(self):
        """function to persist data to a new .csv file"""
        data = pd.read_csv("dataset.csv")
        # reading data in .csv file
        file = input("Name of new file: ")
        # getting name for new file to persist data to
        data.to_csv(file + ".csv", index=False)
        # sending read data to new file
        print("data successfully saved to new file")
        # printing success message

    def print_single_multiple(self):  # Eric Salkovic
        """function to print a single or multiple lines"""
        data = pd.read_csv("dataset.csv")
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
        csvData = pd.read_csv("dataset.csv")
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
        dataFrame.to_csv('dataset.csv', mode='a', index=False, header=False)
        # writing dataframe to .csv file
        print(csvData)
        # printing out new data from .csv file
        print("Data successfully appended")
        # printing success message

    def edit_entry(self):  # Eric Salkovic
        """function to edit a row in .csv file"""
        try:
            # try/except in case of failure
            data = pd.read_csv("dataset.csv")
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
            data.to_csv("dataset.csv", index=False)
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
            data = pd.read_csv("dataset.csv")
            # reading data from .csv file
            print(data)
            # printing data to see the first and last 5 rows (to easily see newly added rows)
            row = input("What row # would you like to delete? ")
            # promting user for which row to delete
            data = data.drop(data.index[int(row)])
            # executing delete/drop row in .csv file
            data.to_csv("dataset.csv", index=False)
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
        """function to sort csv file into a data dictionary and print out all records"""
        # opening dataset to convert into data dictionary
        with open("dataset.csv", 'r') as data:
            # dictionary reader
            dict_reader = DictReader(data)
            # converting data into a dictionary
            dict_list = list(dict_reader)
            # printing .csv headers as keys for the dictionary
            print(dict_list[0].keys())
            # row counter
            count = 1
            # printing each row from the dictionary
            for row in dict_list:
                print(count, f" REF_DATE: {row['ï»¿REF_DATE']}, GEO: {row['GEO']}, DGUID: {row['DGUID']}, Area & Production &"
                      f" farm value of potatoes: {row['Area_production_and_farm_value_of_potatoes']}, UOM: {row['UOM']},"
                      f" UOM_ID: {row['UOM_ID']}, SCALAR FACTOR: {row['SCALAR_FACTOR']}, SCALAR ID: {row['SCALAR_ID']},"
                      f" VECTOR: {row['VECTOR']}, COORDINATE: {row['COORDINATE']}, VALUE {row['VALUE']}, STATUS: "
                      f"{row['STATUS']}, SYMBOL: {row['SYMBOL']}, TERMINATED: {row['TERMINATED']}, DECIMALS: {row['DECIMALS']}")
                # incrementing the count by 1
                count += 1
            # printing number of rows
            print(count - 1, " rows")

    def new_dict_record(self):
        """function to add a new record to the data dictionary and re-write it to the csv file"""
        # opening dataset to convert into data dictionary
        with open("dataset.csv", 'r') as data:
            # dictionary reader
            dict_reader = DictReader(data)
            # converting data into a dictionary
            dict_list = list(dict_reader)
        # prompting user to enter the values for a new record in the data dictionary
        print("Inserting new row in .csv data dictionary")
        new_ref_date = input("What is the new REF_DATE value? ")
        new_dguid = input("What is the new DGUID value? ")
        new_geo = input("What is the new GEO value? ")
        new_area = input("What is the new Area value? ")
        new_uom = input("What is the new UOM value? ")
        new_uom_id = input("What is the new UOM_ID value? ")
        new_scalar_factor = input("What is the new SCALAR FACTOR value? ")
        new_scalar_id = input("What is the new SCALAR ID value? ")
        new_vector = input("What is the new VECTOR value? ")
        new_coordinate = input("What is the new COORDINATE value? ")
        new_value = input("What is the new VALUE value? ")
        new_status = input("What is the new STATUS value? ")
        new_symbol = input("What is the new SYMBOL value? ")
        new_terminated = input("What is the new TERMINATED value? ")
        new_decimals = input("What is the new DECIMALS value? ")
        # creating new dictionary with the given values to be entered as a record in original dictionary
        new_dict_record = {
            'ï»¿REF_DATE': new_ref_date,
            'DGUID': new_dguid,
            'GEO': new_geo,
            'Area_production_and_farm_value_of_potatoes': new_area,
            'UOM': new_uom,
            'UOM_ID': new_uom_id,
            'SCALAR_FACTOR': new_scalar_factor,
            'SCALAR_ID': new_scalar_id,
            'VECTOR': new_vector,
            'COORDINATE': new_coordinate,
            'VALUE': new_value,
            'STATUS': new_status,
            'SYMBOL': new_symbol,
            'TERMINATED': new_terminated,
            'DECIMALS': new_decimals
        }
        # inserting the new record into the data dictionary
        dict_list.append(new_dict_record)
        # printing each row from the dictionary
        for row in dict_list:
            print(f"REF_DATE: {row['ï»¿REF_DATE']}, GEO: {row['GEO']}, DGUID: {row['DGUID']}, Area & Production &"
                  f" farm value of potatoes: {row['Area_production_and_farm_value_of_potatoes']}, UOM: {row['UOM']},"
                  f" UOM_ID: {row['UOM_ID']}, SCALAR FACTOR: {row['SCALAR_FACTOR']}, SCALAR ID: {row['SCALAR_ID']},"
                  f" VECTOR: {row['VECTOR']}, COORDINATE: {row['COORDINATE']}, VALUE {row['VALUE']}, STATUS: "
                  f"{row['STATUS']}, SYMBOL: {row['SYMBOL']}, TERMINATED: {row['TERMINATED']}, DECIMALS: {row['DECIMALS']}")

    def edit_record_dict(self):
        """function to edit an existing record in the data dictionary and re-write it all to the csv file"""
        # opening dataset to convert into a dictionary
        with open("dataset.csv", 'r') as data:
            # dictionary reader
            dict_reader = DictReader(data)
            # converting data into a dictionary
            dict_list = list(dict_reader)
            # prompting user to enter the row/record they want to edit
            single_dict = input("What record (row) would you like to edit?")
            try:
                # checking if the row entered is in the dictionary
                if int(single_dict) > len(dict_list):
                    pass
                else:
                    # if the row IS in the dictionary, prompt user to enter the new values to edit the record
                    new_ref_date = input("What is the new REF_DATE value? ")
                    new_dguid = input("What is the new DGUID value? ")
                    new_geo = input("What is the new GEO value? ")
                    new_area = input("What is the new Area value? ")
                    new_uom = input("What is the new UOM value? ")
                    new_uom_id = input("What is the new UOM_ID value? ")
                    new_scalar_factor = input("What is the new SCALAR FACTOR value? ")
                    new_scalar_id = input("What is the new SCALAR ID value? ")
                    new_vector = input("What is the new VECTOR value? ")
                    new_coordinate = input("What is the new COORDINATE value? ")
                    new_value = input("What is the new VALUE value? ")
                    new_status = input("What is the new STATUS value? ")
                    new_symbol = input("What is the new SYMBOL value? ")
                    new_terminated = input("What is the new TERMINATED value? ")
                    new_decimals = input("What is the new DECIMALS value? ")
                    # inserting new values into the chosen record
                    dict_list[int(single_dict)-2]['ï»¿REF_DATE'] = new_ref_date
                    dict_list[int(single_dict)-2]['DGUID'] = new_dguid
                    dict_list[int(single_dict)-2]['GEO'] = new_geo
                    dict_list[int(single_dict)-2]['Area_production_and_farm_value_of_potatoes'] = new_area
                    dict_list[int(single_dict)-2]['UOM'] = new_uom
                    dict_list[int(single_dict)-2]['UOM_ID'] = new_uom_id
                    dict_list[int(single_dict)-2]['SCALAR_FACTOR'] = new_scalar_factor
                    dict_list[int(single_dict)-2]['SCALAR_ID'] = new_scalar_id
                    dict_list[int(single_dict)-2]['VECTOR'] = new_vector
                    dict_list[int(single_dict)-2]['COORDINATE'] = new_coordinate
                    dict_list[int(single_dict)-2]['VALUE'] = new_value
                    dict_list[int(single_dict)-2]['STATUS'] = new_status
                    dict_list[int(single_dict)-2]['SYMBOL'] = new_symbol
                    dict_list[int(single_dict)-2]['TERMINATED'] = new_terminated
                    dict_list[int(single_dict)-2]['DECIMALS'] = new_decimals
                    print("Record Successfully Edited")
                    # using open dataset to write the data back into the .csv file
                    with open("dataset.csv", 'w', newline='') as data:
                        # creating the dictionary writer
                        dict_writer = csv.DictWriter(data, fieldnames=dict_list[0].keys())
                        # writing the headers
                        dict_writer.writeheader()
                        # rewriting the dictionary back to .csv file
                        dict_writer.writerows(dict_list)
                # printing row that was edited
                print(dict_list[int(single_dict)-2])
                # closing dataset
                data.close()
            # exception handling if the user enters a row that does not exist in the dataset.
            except IndexError:
                # printing error messsage
                print("IndexError Exception: Index out of range")

    def delete_single_dict(self):
        """function to delete an existing record in the data dictionary and re-write it all to the csv file"""
        # prompting user to enter the record/row they want to delete
        del_single_rec = input("Which record (row) would you like to delete?")
        # using open dataset
        with open("dataset.csv", 'r') as data:
            # creating dictionary reader
            dict_reader = DictReader(data)
            # converting data into a dictionary
            dict_list = list(dict_reader)
            # checking if the record exists in the dictionary
            if int(del_single_rec) <= len(dict_list):
                # deletes chosen record
                del_rec = dict_list.pop(int(del_single_rec) - 2)
                # printing
                print("Following record successfully deleted:")
                # printing the record that was deleted
                print(del_rec)
            else:
                # printing appropriate error message
                print("Record does not exist")
        # opening dataset to write into it
        with open("dataset.csv", 'w', newline='') as data:
            # getting header values for the keys
            fieldnames = dict_list[0].keys()
            # creating the dictionary writer
            dict_writer = csv.DictWriter(data, fieldnames=fieldnames)
            # writing the header values
            dict_writer.writeheader()
            # rewriting the dictionary back to .csv file
            dict_writer.writerows(dict_list)

    def sort_multiple(self): # Eric Salkovic
        """function to sort and print a single or multiple rows based on user input"""
        # making a dataframe from the csv file
        df = pd.read_csv("dataset.csv")
        # printing column names for user to select from
        print(df.columns)
        # getting single or multiple column names to print out
        selected_col = input("Enter column name(s) you want to print (separated by a comma and no spaces)")
        # in the case where user enters multiple, this will split the columns
        selected_col = selected_col.split(",")
        # creating secondary dataframe of selected row(s)
        selected_df = df[selected_col]
        # printing the secondary dataframe
        print(selected_df.head())

