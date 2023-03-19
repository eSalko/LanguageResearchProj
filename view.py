from model import MenuFunctions


class MakeMenu:
    """MakeMenu class containing the formatting and printing of the menu to
    display to the user on application start"""
    def printMenu(self):
        """function to print menu"""
        menuFunction = MenuFunctions()
        # creating MenuFunctions object to access available functions
        menuFunction.make_menu()
        # calling menu function to show the user a menu
        option = input("What would you like to do? ")
        # getting input from user to select a menu option
        match option:
            # match/case decision structure to execute selected menu option
            case "1":
                # case 1 to print all data
                menuFunction.print_data()
            case "2":
                # case 2 to print metadata
                menuFunction.print_metadata()
            case "3":
                # case 3 to print 20 rows
                menuFunction.print_20()
            case "4":
                # case 4 to exit application
                menuFunction.print_name()
                exit()
            case "5":
                # case 5 to reload the dataset
                menuFunction.reload_dataset()
            case "6":
                # case 6 to persist data to new file
                menuFunction.persist_new()
            case "7":
                # case 7 to print 1 or more rows
                menuFunction.print_single_multiple()
            case "8":
                # case 8 to create new entry
                menuFunction.create_entry()
            case "9":
                # case 9 to edit existing entry
                menuFunction.edit_entry()
            case "10":
                # case 10 to delete existing entry
                menuFunction.delete_entry()
            case "11":
                # case 11 to sort csv data
                menuFunction.sort_dict()
            case "12":
                # case 12 to insert a new record into dictionary
                menuFunction.new_dict_record()
            case "13":
                # case 13 to select display and edit record in dictionary
                menuFunction.edit_record_dict()
            case "14":
                # case 14 to delete a record from dictionary
                menuFunction.delete_single_dict()

        print()
        # printing empty line to look cleaner
        menuFunction.print_name()
        # printing my name to prove this is my original work
