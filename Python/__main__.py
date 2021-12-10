from personna import * 

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
        print(Pointeur.show_address())
        print("--")

def Test_instance():
    Test = Personna("Test prenom", "Test nom")
    Pointeur = Personna("Theo", "La remorque")
    Pointeur.set_address("10", "rue de la betonniere", "Grenoble", "35010")
    if isinstance(Test, object):
        print("Object has been initialized")
        print(Pointeur.__str__())
        print(Pointeur.show_address())
        print("================================")
    else:
        return "[ERROR] Object has not been initialized"

answer = input("Test ou Start : ")
while answer != "Test" or answer != "Start":
    if answer == "Test":
        Test_instance()
        break
    elif answer == "Start":
        Launch_list_habitant()
        break
    answer = input("Test ou Start : ") 
