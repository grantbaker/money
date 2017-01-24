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

VERBOSE = 0

try:
    (opts, args) = getopt.getopt(sys.argv[1:],"v:")
except getopt.GetoptError:
    print("Invalid options. Exiting...")
    sys.exit()
for (opt, arg) in opts:
    if (opt in ("-v", "--verbose")):
        if (arg in ('0', '1','2','3')):
            VERBOSE = int(arg)
        else:
            print("Invalid options. Exiting...")
            sys.exit()
        print("Entering verbose mode: Level " + arg + ".")
        print("Level 0: Normal outputs")
        print("Level 1: Basic diagnostics")
        print("Level 2: All diagnostics")
        print("Level 3: Special use. Not typically implemented")


class Entry:

    timestamp = -1;

    def __init__(self):
        timestamp = int(1000*round(time(),3));
        if VERBOSE >= 2: print("V2: Entry timestamp: " + str(timestamp))





def enter_expense():
    if VERBOSE >= 1: print("V1: In expense function")

def update_investments():
    if VERBOSE >= 1: print("V1: In inventment function")

def exit_program():
    if VERBOSE >= 1: print("V1: In exit program")
    sys.exit()

in_main_menu = 1;
menu_entries = ["0: Exit","1: Enter Expense","2: Update Investments Value"];
menu_functions = {
    0: exit_program,
    1: enter_expense,
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
        if int(menu_selection) == 0:
            break
    if valid_input == 0:
        print("Invalid input.")
        continue
    if VERBOSE >= 2: print("Valid input.")
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
