# FOR READING THE FILES and sorting.... 
# method 1.
#   
# with open("names.csv") as file:
#     for name in sorted(file):
#        sept = name.rstrip().split(",")
#        print(f"{sept[0]} is in house{sept[1]}")
 
# # # method 2.
# with open("names.csv") as file:
#     for names in sorted(file):
#        name,house = names.rstrip().split(",")
#        print(f"{name} is in house{house}")

# However, both of these methods sort the entire line alphabetically,
# rather than sorting based on the 'name' or 'house' values.

# method 3.

details = []
with open("names.csv") as file:
    for names in file:
        name,house = names.rstrip().split(",")
        detail = {"name":name,"house":house}
        details.append(detail)

def get_key(detail):    
    return detail["name"]

for detail in sorted(details, key = get_key):
    print(f"{detail['name']} is in {detail['house']}")