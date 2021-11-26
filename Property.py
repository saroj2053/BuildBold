class Property:
    property_name = []
    property_address = []

    def add_property(self, property_name, property_address):
        self.property_name.append(input("Enter the property name\n"))
        self.property_address.append(input("Enter the location of the property\n"))
