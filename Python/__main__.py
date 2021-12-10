from personna import *
from test import *

def Launch_list_habitant():
    for element in range(0, 3 + 1):
        Pointeur = Personna(
            habitant_list[element]["first_name"], 
            habitant_list[element]["last_name"]
        )
        Pointeur.set_address(
            habitant_list[element]["address_number"],
            habitant_list[element]["address_street"],
            habitant_list[element]["city"],
            habitant_list[element]["postcode"],
        )
        print(Pointeur.__str__())
        Pointeur.show_address()
        print("--")

answer = input("Test ou Start : ")
while answer != "Test" or answer != "Start":
    if answer == "Test":
        PointerTest = TestPersonna()
        break
    elif answer == "Start":
        Launch_list_habitant()
        break
    answer = input("Test ou Start : ") 
