import datetime


def get_int(prompt):
    """
    Get an integer from the user.
    Params:
        prompt: The prompt to display to the user.
    Returns:
        The integer entered by the user.
    """
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
    """
    Get the number of people flying.
    Returns:
        Integer: The number of people flying.
    """
    while True:
        people = get_int("How many people will be flying?\n")
        if people < 1:
            print("You must have at least 1 person")
        else:
            break
    return people


def seat_type():
    """
    Get the type of seat the user wants.
    Returns:
        Dictionary: The type of seat and the price of the seat.
    """
    while True:
        seat = {"type": "", "price": 0}
        seat["type"] = input(
            "What type of seating would you like? ((E)conomy, (B)usiness, (F)irst)\n"
        )
        seat["type"] = seat["type"].lower()
        if (
            seat["type"] != "economy"
            and seat["type"] != "business"
            and seat["type"] != "first"
            and seat["type"] != "e"
            and seat["type"] != "b"
            and seat["type"] != "f"
        ):
            print("Invalid input - please enter Economy, Business, or First")
        match (seat["type"]):
            case "economy" | "e":
                seat["price"] = 916
                seat["type"] = "Economy"
                break
            case "business" | "b":
                seat["price"] = 2650
                seat["type"] = "Business"
                break
            case "first" | "f":
                seat["price"] = 5103
                seat["type"] = "First"
                break
    return seat


def luggage_number():
    """
    Get the number of bags the user will be checking in.
    Returns:
        Integer: The number of bags the user will be checking in.
    """
    while True:
        luggage = get_int("How many bags will you be checking in?\n")
        if luggage < 0:
            print("It can not be negative")
        else:
            break
    return luggage


def frequent_flyer():
    """
    Get if the user is a frequent flyer.
    Returns:
        String: The user's answer.
    """
    while True:
        frequent = input("Are you a frequent flyer? (Y/N)\n")
        frequent = frequent.lower()
        if frequent != "y" and frequent != "n":
            print("Invalid input")
        else:
            break
    return frequent


def print_receipt(people, seat, luggage, frequent):
    """
    Print the receipt for the user.
    Params:
        people: The number of people flying.
        seat: The type of seat and the price of the seat.
        luggage: The number of bags the user will be checking in.
        frequent: The user's answer.
    """
    luggage_price = 50
    tax = 0.095
    frequent_discount = 0.1
    print("\nThank you for your reservation")
    print("Date and time:\t\t", datetime.datetime.now())
    print("Number of Seats:\t", people)
    print("Type of Seat:\t\t", seat["type"])
    print(f"Seat(s) price:\t\t {(people * seat['price']):.2f}")
    print("Number of Bags:\t\t", luggage)
    print(f"Luggage(s) price:\t {(luggage * luggage_price):.2f}")
    subtotal = people * seat["price"] + luggage * luggage_price
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
    """
    Get if the user wants to continue the program.
    Returns:
        String: The user's answer.
    """
    cont = input("Would you like to continue? (Y/N)\n")
    cont = cont.lower()
    if cont != "y" and cont != "n":
        print("Invalid input")
        continue_program()
    return cont


def main():
    """
    The main function with the while loop to call each function.
    """
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
