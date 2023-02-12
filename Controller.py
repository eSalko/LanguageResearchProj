from view import MakeMenu


class Main:
    """Main driver class for application and MVC pattern controller class"""
    makeMenu = MakeMenu()
    # instantiating and initializing MakeMenu object to print menu and begin application
    makeMenu.printMenu()
    # calling printMenu() function to print menu and prompt user to choose an option
