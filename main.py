from MenuFunctions import MenuFunctions

# creating MenuFunctions object to access available functions
new_menu = MenuFunctions()

# calling menu function to show the user a menu
new_menu.make_menu()

# getting input from user to select a menu option
option = input("What would you like to do? ")

# instantiating name and student nubmer to print out later in program
name = "Eric Salkovic"
studentnum = "040861953"

# match/case decision structure to execute selected menu option
match option:
    case "1":
        new_menu.print_data()
    case "2":
        new_menu.print_metadata()
    case "3":
        new_menu.print_20()
    case "4":
        print("Program by: " + name + " | " + studentnum)
        exit()

# printing my name to prove it's my original work
print("Program by: " + name + " | " + studentnum)