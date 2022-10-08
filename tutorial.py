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
        add_url = get_url()
        add_tutorial(add_url)
    elif selection == '3':
        update_url = get_url()
        time = get_time()
        update_progress(update_url, time)
    elif selection == '4':
        complete_url = get_url()
        complete_tutorial(complete_url)
    elif selection == '5':
        delete_url = get_url()
        delete_tutorial(delete_url)
    elif selection == '6':
        print("Goodbye!")
    else:
        print("Error. Invalid selection")


    


main()



