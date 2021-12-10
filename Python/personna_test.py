from personna import *

class TestPersonna:
    def __init__(self):
        Test = Personna("Test prenom", "Test nom")
        Pointeur = Personna("Theo", "La remorque")
        Pointeur.set_address("10", "rue de la betonniere", "Grenoble", "35010")
        if isinstance(Test, object):
            print("Object has been initialized")
            print(Pointeur.__str__())
            Pointeur.show_address()
            print("--")
        else:
            print("[ERROR] Object has not been initialized")
