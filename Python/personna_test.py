from personna import *
import unittest

class TestPersonna:
    def __init__(self):
        Pointeur = Personna("Theo", "La remorque")
        Pointeur.set_address("10", "rue de la betonniere", "Grenoble", "35010")
        if isinstance(Pointeur, object):
            print("Object has been initialized")
            print(Pointeur.__str__())
            Pointeur.show_address()
            print("--")
        else:
            print("[ERROR] Object has not been initialized")

class PersonnaTest(unittest.TestCase):
    def test_initialization_object(self):
        Test = Personna("Theo", "La remorque")
        self.assertEqual(Test.__str__(), "Hi ! I'm Theo La remorque")
    
    def test_set_address(self):
        Test = Personna("Theo", "La remorque")
        Test.set_address("10", "rue de la betonniere", "Grenoble", "35010")
        self.assertEqual(Test.show_address(), "My full address is : 10 rue de la betonniere, Grenoble (35010)")

