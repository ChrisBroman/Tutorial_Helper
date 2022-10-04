from functions import *
from classes import *

def main():
    check_file()
    print("Please select an option\n")
    print("1. List current tutorials")
    print("2. Add a tutorial")
    print("3. Update tutorial progress")
    print("4. Complete a tutorial")
    print("5. Delete a tutorial")
    print("6. Exit")
    selection = input("Selection: ")
    print("\n\n")

    if selection == '1':
        list_tutorials()
    elif selection == '2':
        add_url = input("Enter full URL of tutorial: ")
        add_tutorial(add_url)
    elif selection == '3':
        update_url = input("Enter full URL of tutorial: ")
        time = input("Tutorial time (hh:mm:ss): ")
        update_progress(update_url, time)
    elif selection == '4':
        complete_url = input("Tutorial URL: ")
        complete_tutorial(complete_url)
    elif selection == '5':
        delete_url = input("Enter a full URL to delete: ")
        delete_tutorial(delete_url)
    elif selection == '6':
        print("Goodbye!")
    else:
        print("Error. Invalid selection")


    


main()



