# Part 1:
# # 1. Parse out the item (i.e. "apples") in the string below. Use the lecture notes if you need help! Use print statements to help you test along the way.

grocery_string = "item:apples,quantity:4,price:1.50\n"

split_string = grocery_string.split(",") #split_string = ['item:apples', 'quantity:4', 'price:1.50\n']
item_data = split_string[1] #item_data = 'item:apples'
item_split = item_data.split(":") #item_split = ['item', 'apples']
item = item_split[1] #item = 'apples'

# # Part 2:
# # 1. Create a variable called my_name and set it equal to your name. Turn your name into a list of letters using the list() function.

my_name = "Molly"
my_name_list = list(my_name) #my_name_list = ['M', 'o', 'l', 'l', 'y']

# # 2. Turn this string "1,2,3,4,5" into a list of integers using .split() method.

final_list = []
string = "1,2,3,4,5"
string_split = string.split(",") #string_split = ['1', '2', '3', '4', '5']
for item in string_split:
    final_list.append(int(item)) #final_list = [1, 2, 3, 4, 5]

# # 3. Turn the string "One fish two fish red fish blue fish" into a list that looks like ["one", "two", "red", "blue"]

list1 = []
string = "One fish two fish red fish blue fish"
string_split = string.split(" ")
for item in string_split:
    list1.append(item)
del list1[1:8:2]

# 4. Create a function that calculates and returns a person's grocery bill from this string:

def grocery_bill():
    grocery_string = "item:apples,quantity:4,price:1.50\n"
    grocery_split = grocery_string.split(",")
    quantity_data = grocery_split[1]
    quantity_split = quantity_data.split(":")
    quantity = int(quantity_split[1])

    price_data = grocery_split[2]
    price_split = price_data.split(":")
    price_raw = price_split[1]
    price = float(price_raw.strip())

    total = quantity * price
    return total

grocery_bill()

# 5.Modify this program to calculate a person's total grocery bill from the list:

grocery_list = ["item:apples,quantity:4,price:1.50\n",
                "item:pears,quantity:5,price:2.00\n",
                "item:cereal,quantity:1,price:4.49\n"]

def grocery_bill():
    item1 = grocery_list[0]
    grocery_split1 = item1.split(",")
    quantity_data1 = grocery_split1[1]
    quantity_split1 = quantity_data1.split(":")
    quantity1 = int(quantity_split1[1])

    price_data1 = grocery_split1[2]
    price_split1 = price_data1.split(":")
    price_raw1 = price_split1[1]
    price1 = float(price_raw1.strip())

    item2 = grocery_list[1]
    grocery_split2 = item2.split(",")
    quantity_data2 = grocery_split2[1]
    quantity_split2 = quantity_data2.split(":")
    quantity2 = int(quantity_split2[1])

    price_data2 = grocery_split2[2]
    price_split2 = price_data2.split(":")
    price_raw2 = price_split2[1]
    price2 = float(price_raw2.strip())

    item3 = grocery_list[2]
    grocery_split3 = item3.split(",")
    quantity_data3 = grocery_split3[1]
    quantity_split3 = quantity_data3.split(":")
    quantity3 = int(quantity_split3[1])

    price_data3 = grocery_split3[2]
    price_split3 = price_data3.split(":")
    price_raw3 = price_split3[1]
    price3 = float(price_raw3.strip())


    total = (quantity1 * price1) + (quantity2 * price2) + (quantity3 * price3)
    return total

print grocery_bill()







