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

class Account:

    def __init__(self):
        print("account created....")

class Exp_Account(Account):

    def __init__(self):
        Account.__init__(self)
        print("debit account created")

class Cash_Account(Account):

    def __init__(self):
        Account.__init__(self)
        print("cash account created")


class Entry:

    timestamp = -1
    title = None
    amount = None
    method = None
    desc = None
    labels = ["global"]

    def __init__(self):
        timestamp = int(1000*round(time(),3));
        if VERBOSE >= 2: print("V2: Entry timestamp: " + str(timestamp))

    def set_title(self, title_in):
        self.title = title_in

    def set_amount(self, amount_in):
        self.amount = amount_in

    def set_method(self, method_in):
        self.method = method_in

    def set_desc(self, desc_in):
        self.desc = desc_in

    def set_big_three(self, title_in, amount_in, method_in):
        self.title = title_in
        self.amount = amount_in
        self.method = method_in

    def add_labels(self,label_array):
        self.labels.extend(label_array)

    def print_labels(self):
        for l in self.labels:
            print(l)

    def print_all(self):
        if self.title != None: print("TITLE: " + self.title)
        if self.amount != None: print("AMOUNT: $" + str(self.amount))
        if self.desc != None: print("DESCRIPTION: " + self.desc)



def exit_program():
    if VERBOSE >= 1: print("V1: In exit program")
    sys.exit()

def get_amount():
    amount_in = input("AMOUNT: $")
    try:
        amount = float(amount_in)
    except ValueError:
        print("Must be a number.")
        return get_amount()
    return amount

def enter_expense():
    if VERBOSE >= 1: print("V1: In expense function")
    title = input("TITLE: ")
    amount = get_amount()
    method = input("METHOD: ")
    desc = input("DESCRIPTION: ")
    labels = str.split(input("LABELS: "))

    ee = Entry()
    ee.set_big_three(title,amount,method)

    ee.add_labels(labels)
    ee.print_labels()
    ee.print_all()


def update_investments():
    if VERBOSE >= 1: print("V1: In inventment function")

def test_function():
    card = Exp_Account();

def print_accounts():
    if VERBOSE >= 1: print("V1: In print accounts function")

in_manage_accounts = 1;
accounts_menu_entries = ["0: Return to Main Menu","1: Print all accounts"]
accounts_menu_functions = {
    1: print_accounts
}

def manage_accounts():
    if VERBOSE >=1: print("V1: In manage accounts function")
    print("=== MANAGE ACCOUNTS ===")
    for menu_item in accounts_menu_entries:
        print(menu_item)
    print("- - -")
    menu_selection = input("~:")
    try:
        menu_selection = int(menu_selection)
    except ValueError:
        print("Invalid input.")
        manage_accounts()
        return
    print("=======================")
    valid_input = 0
    for test_input in accounts_menu_entries:
        if menu_selection == int(test_input[0]):
            valid_input = 1
        if menu_selection == 0:
            return
    if valid_input == 0:
        print("Invalid input.")
        manage_accounts()
        return
    if VERBOSE >= 2: print("V2: Valid input.")
    accounts_menu_functions[int(menu_selection)]()
    manage_accounts()


in_main_menu = 1;
main_menu_entries = ["0: Exit","1: Enter Expense","2: Update Investments Value","3: Manage Accounts","4: Test"];
main_menu_functions = {
    0: exit_program,
    1: enter_expense,
    2: update_investments,
    3: manage_accounts,
    4: test_function
}

while in_main_menu:
    print("=== MONEY MENU ===")
    for menu_item in main_menu_entries:
        print(menu_item)
    print("- - -")
    menu_selection = input("~:")
    try:
        menu_selection = int(menu_selection)
    except ValueError:
        print("Invalid input.")
        continue
    print("==================")
    valid_input = 0;
    for test_input in main_menu_entries:
        if menu_selection == int(test_input[0]):
            valid_input = 1;
        if menu_selection == 0:
            break
    if valid_input == 0:
        print("Invalid input.")
        continue
    if VERBOSE >= 2: print("V2: Valid input.")
    main_menu_functions[int(menu_selection)]()



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
