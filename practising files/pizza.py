# outputting the csv file in a pretty format

import sys
import csv 
from tabulate import tabulate 

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too man command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv File")
items=[]
try:
    with open(sys.argv[1]) as file:
        reader=csv.reader(file)
        for i in reader:
            items.append(i)
    print(tabulate(items,headers="firstrow",tablefmt="grid"))
            
except FileNotFoundError:
    sys.exit("File does not exist")
