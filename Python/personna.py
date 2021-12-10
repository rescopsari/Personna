habitant = [{
"first_name":"Ilyès",
"last_name":"Fleury",
"address_street":"Rue Paul Bert",
"address_number":73,
"city":"Dunkerque",
"postcode":12681
},{
"first_name":"Lia",
"last_name":"Dumont",
"address_street":"Rue Louis-Blanqui",
"address_number":30,
"city":"Lille",
"postcode":63996
},{
"first_name":"Eléonore",
"last_name":"Caron",
"address_street":"Avenue du Château",
"address_number":87,
"city":"Rennes",
"postcode":78482
},{
"first_name":"Eva",
"last_name":"Girard",
"address_street":"Rue du Bon-Pasteur",
"address_number":9,
"city":"Rueil-Malmaison",
"postcode":23879
}]

class Personna:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._address_street = ""
        self._address_number = 0
        self._city = ""
        self._postcode = ""

    def __str__(self):
        return f"Hi ! I'm { self._first_name } { self._last_name }"

    def show_address(self):
        return f"My full address is : { self._address_number } { self._address_street }, { self._city } ({ self._postcode })"

    def set_address(self,address_number, address_street,city,postcode):
        self._address_street = address_street 
        self._address_number = address_number
        self._city = city 
        self._postcode = postcode 

def Start():
    for element in range(0,3+1):
        Pointeur = Personna(habitant[element]['first_name'], habitant[element]['last_name'])
        Pointeur.set_address(habitant[element]['address_number'], habitant[element]['address_street'], habitant[element]['city'], habitant[element]['postcode'])
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


Test_instance()
Start()
