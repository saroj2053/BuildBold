class Booking:
    username = []
    name_property = []

    def add_booking(self, name, prop_name):
        self.username.append(input("Enter name of the user who has done booking\n"))
        self.name_property.append( input("Enter name of property for which booking has been done\n"))
