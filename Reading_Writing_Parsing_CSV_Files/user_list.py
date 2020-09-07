"""
121
 Create a program that will allow the user to easily manage a list of names.
 You should display a menu that will allow them to add a name to the list,
 change a name in the list, delete a name from the list or view all the names in the list.
 There should also be a menu option to allow the user to end the program.
 If they select an option that is not relevant, then it should display a suitable message.
 After they have made a selection to either add a name, change a name, delete a name or
 view all the names, they should see the menu again
 without having to restart the program.
 The program should be made as easy to use as possible
"""


def add_name(names):
    name_to_add = input("Enter the name you wish to add: ")
    names.append(name_to_add)


def change_name(names):

    change = input("Which name do you wish to change?: ")
    new_name = input("Please enter the new name?: ")
    if change in names:
        names[names.index(change)] = new_name

def del_name(names):
    delete = input("Which name do you wish to remove?: ")
    if delete in names:
        names.remove(delete)

def view_names(names):
    for i in names:
        print(i)


def main():
    names = []
    again = 'y'
    while again == 'y':
        print("What do you wish to do?")
        print("\t1. Add name?\n\t2. Change name?\n\t3. Delete name?\n\t4. View names\n\t5. Quit")
        user_input = input("Please select: ")
        if user_input == '1':
            add_name(names)
            # print(names)
        elif user_input == '2':
            change_name(names)
            # print(names)
        elif user_input == '3':
            del_name(names)
            # print(names)
        elif user_input == '4':
            view_names(names)

        elif user_input == '5':
            again = 'n'
        else:
            print('wrong input')


if __name__ == '__main__':
    main()
