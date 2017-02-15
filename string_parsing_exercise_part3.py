# Part 3:
# Let's improve our Shopping List program: You'll be using your existing shopping list project or you can click 'Download' in this exerciser's portal listing for a fresh start. We'll continue adding onto this project over the next few lectures so make sure to push it to your Github at the end of class. Let's make this program better by allowing the user to input more than one item at a time, by way of a comma separated string.
# 1. Add a function that parses a comma separated string. Make sure to deal with white spaces. Take a moment to write some pseudocode with your partner! It's always nice to have a plan to refer back to.
# 2. Inside your main() function, add logic where you add an item to the shopping list. This is where you will call the new function you just wrote.


def menu():
    menu_list = ["0", "1", "2", "3", "4", "5", "6", "7"]

    print "0 - Main Menu"
    print "1 - Show all lists"
    print "2 - Show a specific list"
    print "3 - Add a new shopping list"
    print "4 - Add an item to a shopping list"
    print "5 - Remove an item from a shopping list"
    print "6 - Remove a list by nickname"
    print "7 - Exit when you are done"

    menu_choice = raw_input("Please select an option: ")

    if menu_choice not in menu_list:
        print "Please enter 0, 1, 2, 3, 4, 5, 6 or 7."
        main()
    else:
        return menu_choice

def show_lists(grocery_lists):
    print "The shopping list items are: "
    for shopping_list, list_items in grocery_lists.items():
        print "%s:" % (shopping_list)
        for item in list_items:
            print "%s:" % (item)
    return

def sorted_lists(grocery_lists, list_name):
    if list_name in grocery_lists:
        sorted_grocery_list = grocery_lists[list_name]
        sorted_grocery_list.sort()
        return sorted_grocery_list
    else:
        return "The shopping list %s does not exist." % (list_name)

def add_list(grocery_lists, new_list):
    if new_list not in grocery_lists:
        grocery_lists[new_list] = []
    else:
        print "List %s already exists!" % (new_list)
    return grocery_lists

def add_item(grocery_lists, list_name, item):
    if list_name in grocery_lists:
        shopping_list = grocery_lists[list_name]
        item = item.lower()
        if item not in shopping_list:
            shopping_list.append(item)
        else:
            print "Item %s is already on the %s list." % (item, list_name)
    else:
        print "There is no %s list." % (list_name)
    return grocery_lists

def remove_list(grocery_lists, list_name):
    if list_name in grocery_lists:
        del grocery_lists[list_name]
        print "The %s list has been removed." % (list_name)
    else:
        print "There is no %s list." % (list_name)

def remove_item(grocery_lists, list_name, item):
    if list_name in grocery_lists:
        shopping_list = grocery_lists[list_name]
        item = item.lower()
        if item in shopping_list:
            shopping_list.remove(item)
            print "Item %s has been removed." % (item)
        else:
            print "Item %s is not on the list." % (item)
    else:
        print "There is no %s list." % (list_name)
    return grocery_lists

def parse_string(string):
    string = string.strip()
    string_split = string.split(",")
    items_list = []
    for item in string_split:
        items_list.append(item.strip())
    return items_list

def main():
    grocery_lists = {}

    while (True):
        menu_choice = menu()

        if menu_choice == "0":
            continue

        elif menu_choice == "1":
            show_lists(grocery_lists)
            
        elif menu_choice == "2":
            list_name = raw_input("Which list would you like to see?: ")
            print sorted_lists(grocery_lists, list_name)

        elif menu_choice == "3":
            list_name = raw_input("What would you like to call your list?: ")
            add_list(grocery_lists, list_name)
            string = raw_input("Please enter items separated by commas: ")
            items = parse_string(string)
            for item in items:
                add_item(grocery_lists, list_name, item)

        elif menu_choice == "4":
            list_name = raw_input("What is the name of the list?: ")
            if list_name in grocery_lists:
                string = raw_input("Please enter items separated by commas: ")
                items = parse_string(string)
                for item in items:
                    add_item(grocery_lists, list_name, item)
            else:
                print "There is no %s list." % (list_name)

        elif menu_choice == "5":
            list_name = raw_input("What is the name of the list?: ")
            if list_name in grocery_lists:
                string = raw_input("Please enter items separated by commas: ")
                items = parse_string(string)
                for item in items:
                    remove_item(grocery_lists, list_name, item)
            else:
                print "There is no %s list." % (list_name)

        elif menu_choice == "6":
            list_name = raw_input("What is the name of the list?: ")
            remove_list(grocery_lists, list_name)

        elif menu_choice == "7":
            break

if __name__ == '__main__':
    main()