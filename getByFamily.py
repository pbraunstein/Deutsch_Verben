#!/usr/bin/env python

# Looks in the DB file for words maching the ending supplied
# on the command line. This script can be used to test all the words with
# this ending or can be used to simply list all of the words.

DB_FILE = "/Users/Phippe/Developer/Self_Betterment"

from sys import exit
from sys import argv
import re
import random

from dl import buildList

def main():
    option = None  # Default
    if len(argv) == 1:  # No options
        print "ERROR: Not enough command line parameters"
        usage()
    elif len(argv) == 2:
        root = argv[1]
    elif len(argv) == 3:
        option = argv[1]
        root = argv[2]
    else:
        print "ERROR: Too many command line parameters"
        usage()

    verbTable = buildList()

    filteredTable = filterVerbTable(verbTable, root)

    if len(filteredTable) == 0:
        print "No verbs match root:", root
        exit(1)

    if not option:
        option = "-t"  # Default behavior

    if option == "-t":
        test(filteredTable)
        view(filteredTable)
    elif option == "-s":
        view(filteredTable)
    else:
        print "ERROR: Invalid option:", option
        usage()

    exit(0)


# Prints usage and exits non-zero
def usage():
    print "USAGE:", argv[0], "-s", "root", "--", "just print"
    print "USAGE:", argv[0], "-t", "root", "--", "test then print"
    print "Default option is -t"
    exit(1)

# Returns a table only with those entries whose first elements
# match .*root$
def filterVerbTable(verbTable, root):
    regEx = re.compile(".*" + root)

    return filter(lambda x: regEx.match(x[0]), verbTable)

# Asks user meaning of all words selected, waiting for enter key input
# to show the answer. Then shows the Hilfsverb + Partizipzwei without being
# prompted. Some basic formatting
def test(data):
    random.shuffle(data)

    def iTest(entry):
        raw_input(entry[0] + ":")
        for defn in entry[2].split(";"):
            print "    " + defn
        print "    " + entry[1]
        print

    map(iTest, data)



# Right now sorts umlauts to the end. Might fix this later
def view(data):
    data.sort(key = lambda x: x[0])
    def printEl(x):
        print x[0] + " --- " + x[2]

    map(printEl, data)


if __name__ == "__main__":
    main()
