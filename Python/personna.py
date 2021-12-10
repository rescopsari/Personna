from habitant import habitant_list
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
        print(f"My full address is : { self._address_number } { self._address_street }, { self._city } ({ self._postcode })")

    def set_address(self, address_number, address_street, city, postcode):
        self._address_number = address_number
        self._address_street = address_street
        self._city = city
        self._postcode = postcode