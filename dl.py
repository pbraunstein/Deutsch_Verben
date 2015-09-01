#!/usr/bin/env python

from sys import argv
from sys import exit
import csv
import random

# CONSTANTS
DB_FILE = "/Users/Phippe/Developer/Self_Betterment/dl.csv"

def main():
    if len(argv) > 1:
        addEntry()
        exit(0)

    data = buildList()

    print "Choosing from", len(data), "words"

    displayAndTest(random.choice(data))
    
    exit(0)

# Reads in DB file into list of lists 
def buildList():
    toReturn = []
    with open(DB_FILE, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            toReturn.append([x.strip() for x in row])

    return toReturn

# Show German word, waits for input, shows English defs, wait for inputs
# shows Partizip II returns
# structure of input as below
# [german, partzip, english1;english2]
def displayAndTest(toTest):
    raw_input("Was bedeutet " + toTest[0] + "?")
    for defin in toTest[2].split(";"):
        print defin
    print
    raw_input("Was ist das Partzip und Hilfsverb?")
    print toTest[1]
    print


# Adds an entry to the current entry in the db
def addEntry():
    entryValid()  # if returns, entry okay

    toAdd = []

    currentData = buildList()

    # create new entry
    defs = argv[4:]
    toAdd.append(argv[2])
    toAdd.append(argv[3])
    toAdd.append(";".join(defs))

    currentData.append(toAdd)

    writeOut(currentData)


# Enforces these invariants:
# 1. First command line arg is exactly -a or -Add
# 2. there are at least 4 args on command line (not including script name)
# Exits with error message if any invariant violated
def entryValid():
    invalid = False
    if len(argv) < 5:
        print "ERROR: Not Enough Arguments Provided"
        print argv
        invalid = True
    elif argv[1] != "-a" and argv[1] != "-Add":
        print "ERROR: Must supply -a or -Add as First Argument"
        invalid = True

    if invalid:
        print "USAGE:", argv[0], "-a", "Deutsches_Verb",
        print "Partizip_mit_Hilfsverb", 
        print "englische_Definitionen (beliebige Zahl)"

        exit(1)


# Overwrites DB_FILE with all the entries in currentData
def writeOut(currentData):
    with open(DB_FILE, 'w') as csvFile:
        csvWriter = csv.writer(csvFile)

        for row in currentData:
            csvWriter.writerow(row)

        print ",".join(currentData[-1])


if __name__ == '__main__':
    main()
