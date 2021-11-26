import Employee
import Customer
import Property as Pty
import Booking

continuation = True


while continuation:
    selection = int(input("Enter 1 to add new employee,"
                          "2 to add new customer, "
                          "3 to add new property, "
                          "4 to add new booking.\n"))

    if selection == 1:
        emp = Employee.Employee()
        emp.add_employee(emp.name, emp.emp_number)

    if selection == 2:
        cust = Customer.Customer()
        cust.add_customer(cust.customer_name)

    if selection == 3:
        props = Pty.Property()
        props.add_property(props.property_name, props.property_address)

    if selection == 4:
        bookings = Booking.Booking()
        bookings.add_booking(bookings.username, bookings.name_property)

    should_continue = input("Do you want to continue? Type yes or no ")

    if should_continue == 'no':
        continuation = False

print("Employee names:\n")
for names in Employee.Employee.name:
    print(names)

print("Customer names:\n")
for users in Customer.Customer.customer_name:
    print(users)

print("Property names:\n")
for assets in Pty.Property.property_name:
    print(assets)

print("Bookings:\n")
for bookings in Booking.Booking.name_property:
    print(bookings)
