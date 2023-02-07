import datetime


def get_int(prompt):
    val = 0
    valid = False
    while not valid:
        try:
            val = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid input - should be an integer.")
    return val


def people_number():
    people = get_int("How many people will be flying?\n")
    if people < 1:
        print("You must have at least 1 person")
        people_number()
    return people


def seat_type():
    seat = {'type': "", 'price': 0}
    seat['type'] = input(
        "What type of seating would you like? ((E)conomy, (B)usiness, (F)irst)\n")
    seat['type'] = seat['type'].lower()
    if seat['type'] != "economy" and seat['type'] != "business" and seat['type'] != "first" and seat['type'] != "e" and seat['type'] != "b" and seat['type'] != "f":
        print("Invalid input - please enter Economy, Business, or First")
        seat_type()
    match (seat['type']):
        case "economy" | "e":
            seat['price'] = 916
            seat['type'] = "Economy"
        case "business" | "b":
            seat['price'] = 2650
            seat['type'] = "Business"
        case "first" | "f":
            seat['price'] = 5103
            seat['type'] = "First"
    return seat


def luggage_number():
    luggage = get_int("How many bags will you be checking in?\n")
    if luggage < 0:
        print("It can not be negative")
        luggage_number()
    return luggage


def frequent_flyer():
    frequent = input("Are you a frequent flyer? (Y/N)\n")
    frequent = frequent.lower()
    if frequent != "y" and frequent != "n":
        print("Invalid input")
        frequent_flyer()
    return frequent


def print_receipt(people, seat, luggage, frequent):
    luggage_price = 50
    tax = 0.095
    frequent_discount = 0.1
    print("\nThank you for your reservation")
    print("Date and time:\t\t", datetime.datetime.now())
    print("Number of Seats:\t", people)
    print("Type of Seat:\t\t", seat['type'])
    print(f"Seat(s) price:\t\t {(people * seat['price']):.2f}")
    print("Number of Bags:\t\t", luggage)
    print(f"Luggage(s) price:\t {(luggage * luggage_price):.2f}")
    subtotal = people * seat['price'] + luggage * luggage_price
    print(f"Subtotal:\t\t {subtotal:.2f}")
    if frequent == "y":
        discount = subtotal * frequent_discount
        print(f"Discount:\t\t {discount:.2f}")
        subtotal = subtotal - discount
        print(f"Subtotal:\t\t {subtotal:.2f}")
    taxes = subtotal * tax
    print(f"Taxes:\t\t\t {taxes:.2f}")
    total = subtotal + taxes
    print(f"Total:\t\t\t {total:.2f}\n")


def continue_program():
    cont = input("Would you like to continue? (Y/N)\n")
    cont = cont.lower()
    if cont != "y" and cont != "n":
        print("Invalid input")
        continue_program()
    return cont


def main():
    while True:
        print("Welcome to the Airline Reservation System")
        print("Round-Trip tickets from Los Angeles, California to Narita, Japan\n")
        people = people_number()
        seat = seat_type()
        luggage = luggage_number()
        frequent = frequent_flyer()
        print_receipt(people, seat, luggage, frequent)
        cont = continue_program()
        if cont == "n":
            break


main()
