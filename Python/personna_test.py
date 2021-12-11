from personna import *

import io
import unittest
import unittest.mock

# class TestPersonna:
#     def __init__(self):
#         Pointeur = Personna("Theo", "La remorque")
#         Pointeur.set_address("10", "rue de la betonniere", "Grenoble", "35010")
#         if isinstance(Pointeur, object):
#             print("Object has been initialized")
#             print(Pointeur.__str__())
#             Pointeur.show_address()
#             print("--")
#         else:
#             print("[ERROR] Object has not been initialized")

class PersonnaTest(unittest.TestCase):
    def test_initialization_object(self):
        # Arrange
        firstname = "Theo"
        lastname = "La remorque"

        # Act
        Test = Personna(firstname, lastname)

        # Assert
        self.assertEqual(Test.__str__(), "Hi ! I'm Theo La remorque")
        
    def test_initialization_object_goodformat(self):
        # Arrange
        firstname = "tHEo"
        lastname = "LA RemORQuE"

        # Act
        Test = Personna(firstname, lastname)

        # Assert
        self.assertEqual(Test.__str__(), "Hi ! I'm Theo La remorque")
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_set_address(self, mock_stdout):
        # Arrange
        firstname = "Theo"
        lastname = "La remorque"

        address_number = "10"
        address_street = "rue de la betonniere"
        city = "Grenoble"
        postcode = "35010"

        # Act
        Test = Personna(firstname, lastname)
        Test.set_address(address_number, address_street, city, postcode)
        Test.show_address()

        # Assert
        self.assertEqual(mock_stdout.getvalue(), "My full address is : 10 rue de la betonniere, Grenoble (35010)\n")
 
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_set_address_goodformat(self, mock_stdout):
        # Arrange
        firstname = "Theo"
        lastname = "La remorque"

        address_number = "10"
        address_street = "RUe dE La bETONNIERE"
        city = "Grenoble"
        postcode = "35010"

        # Act
        Test = Personna(firstname, lastname)
        Test.set_address(address_number, address_street, city, postcode)
        Test.show_address()

        # Assert
        self.assertEqual(mock_stdout.getvalue(), "My full address is : 10 rue de la betonniere, Grenoble (35010)\n")
 