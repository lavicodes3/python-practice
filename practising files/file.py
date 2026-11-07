import csv
import sys
if len(sys.argv)<3:
    sys.exit("too few command line arguments")
elif len(sys.argv)>3:
    sys.exit("too many command line arguments")
if not (sys.argv[2]).endswith(".csv"):
    sys.exit("new file doesnt endswith csv")

students=[]
try:
    with open(sys.argv[1]) as file:
        reader=csv.DictReader(file)
        for row in reader:
            last,first=row["name"].split(", ")
            house=row["house"]
            students.append({"first":first,"last":last,"house":house})
except FileNotFoundError:
    sys.exit("file cant be read")
with open(sys.argv[2],"w") as file:
    fieldname=["first","last","house"]
    write=csv.DictWriter(file,fieldnames=fieldname)
    write.writeheader()
    for i in students:
        write.writerow(i)