#!/usr/bin/python3

import sys, getopt, pickle
from time import time

# print("Number of arguments: %s" % len(sys.argv))
# t = int(1000*round(time(),3));
# print(t);

# def save_object(obj, filename):
#     with open(filename, 'wb') as output:
#         pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#
# with open(filename, 'rb') as input:
#     test2 = pickle.load(input)


class Entry:

    timestamp = -1;

    def __init__(self):
        timestamp = int(1000*round(time(),3));





def enter_expense():
    print("in expense function")

def update_investments():
    print("in inventment function")

in_main_menu = 1;
menu_entries = ["1: Enter Expense","2: Update Investments Value"];
menu_functions = {1: enter_expense,
                  2: update_investments
}

while in_main_menu:
    print("=== MONEY MENU ===")
    for menu_item in menu_entries:
        print(menu_item)
    print("- - -")
    menu_selection = input("~:")
    print("==================")
    valid_input = 0;
    for test_input in menu_entries:
        if menu_selection == test_input[0]:
            valid_input = 1;
    if valid_input == 0:
        print("Invalid input.")
        continue
    print("Valid input.")
    menu_functions[int(menu_selection)]()



# possible_subcommands = ("expense");
# input_error = 1;

# for arg in sys.argv:
#     if arg in possible_subcommands:
#         print(arg)
#         input_error = 0;
#         if arg == "expense":
#             expense();
#
# if input_error == 1:
#     print("Error. Possible subcommands:");
#     for sc in possible_subcommands:
#         print(sc)
