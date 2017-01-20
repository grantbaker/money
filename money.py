#!/usr/bin/python

import sys, getopt, pickle
from time import time

#print("Number of arguments: %s" % len(sys.argv))
#t = int(1000*round(time(),3));
#print(t);

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

with open(filename, 'rb') as input:
    test2 = pickle.load(input)


class Entry:

    timestamp = -1;

    def __init__(self):
        timestamp = int(1000*round(time(),3));





def expense():
    print("in expense function")



possible_subcommands = ("expense");
input_error = 1;

for arg in sys.argv:
    if arg in possible_subcommands:
        print(arg)
        input_error = 0;
        if arg == "expense":
            expense();

if input_error == 1:
    print("Error. Possible subcommands:");
    for sc in possible_subcommands:
        print(sc)
