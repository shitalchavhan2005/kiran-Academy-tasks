
from abc import ABC, abstractmethod


# 1. Base class: Passenger (Abstraction)
class Passenger(ABC):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def get_discount(self):
        pass

    @property
    @abstractmethod
    def passenger_type(self):
        pass


# 2. Child class: RegularPassenger (Inheritance)
class RegularPassenger(Passenger):

    def get_discount(self):
        return 0.0

    @property
    def passenger_type(self):
        return "Regular"


# 3. Child class: StudentPassenger (Inheritance)
class StudentPassenger(Passenger):

    def get_discount(self):
        return 0.10

    @property
    def passenger_type(self):
        return "Student"


# 4. Flight class (Encapsulation)
class Flight:

    def __init__(self, code, airline, source, destination,
                 available_seats, base_fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def book_seats(self, ticket_count):
        if ticket_count <= self.__available_seats:
            self.__available_seats -= ticket_count
            return True
        return False

    def display(self):
        print("-" * 65)
        print(f"Flight Code     : {self.__code}")
        print(f"Airline         : {self.__airline}")
        print(f"Route           : {self.__source} to {self.__destination}")
        print(f"Available Seats : {self.__available_seats}")
        print(f"Base Fare       : Rs. {self.__base_fare:.2f}")


# 5. Booking class
class Booking:

    def __init__(self, booking_id, passenger, flight, ticket_count):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.ticket_count = ticket_count

        self.subtotal = flight.base_fare * ticket_count
        self.discount_amount = (
            self.subtotal * passenger.get_discount()
        )
        self.final_amount = self.subtotal - self.discount_amount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID       :", self.booking_id)
        print("Passenger Name   :", self.passenger.name)
        print("Passenger Age    :", self.passenger.age)
        print("Passenger Type   :", self.passenger.passenger_type)
        print("Flight Code      :", self.flight.code)
        print("Airline          :", self.flight.airline)
        print("Route            :", self.flight.source,
              "to", self.flight.destination)
        print("Number of Tickets:", self.ticket_count)
        print(f"Base Fare/Ticket : Rs. {self.flight.base_fare:.2f}")
        print(f"Subtotal         : Rs. {self.subtotal:.2f}")

        discount_percent = self.passenger.get_discount() * 100

        print(f"Discount ({discount_percent:.0f}%)  : Rs. "
              f"{self.discount_amount:.2f}")
        print(f"Final Amount     : Rs. {self.final_amount:.2f}")
        print("=====================================")


# 6. Main Flight Booking System
class FlightBookingSystem:

    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 25, 2500)
        ]

        self.bookings = []
        self.next_booking_number = 1001

    # Display all available flights
    def display_flights(self):
        print("\n========== AVAILABLE FLIGHTS ==========")

        for flight in self.flights:
            flight.display()

        print("-" * 65)

    # Find a flight using its code
    def find_flight(self, flight_code):
        for flight in self.flights:
            if flight.code.lower() == flight_code.lower():
                return flight

        return None

    # Validate booking information
    def validate_booking(self, flight, name, age, ticket_count):
        if flight is None:
            print("Booking failed: Invalid flight code.")
            return False

        if not name.strip():
            print("Booking failed: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Booking failed: Age must be greater than 0.")
            return False

        if ticket_count <= 0:
            print("Booking failed: Ticket count must be greater than 0.")
            return False

        if ticket_count > flight.available_seats:
            print("Booking failed: Not enough seats available.")
            return False

        return True

    # Calculate and confirm a booking
    def confirm_booking(self, flight, passenger, ticket_count):
        # Create booking details before changing the seat count
        booking = Booking(
            "BK" + str(self.next_booking_number),
            passenger,
            flight,
            ticket_count
        )

        # Reduce seats only after validation succeeds
        if flight.book_seats(ticket_count):
            self.bookings.append(booking)
            self.next_booking_number += 1

            print("\nBooking confirmed!")
            booking.display_summary()
        else:
            print("Booking failed: Not enough seats available.")

    # Take booking input from the user
    def book_flight(self):
        print("\n========== BOOK A FLIGHT ==========")

        flight_code = input("Enter flight code: ").strip()
        flight = self.find_flight(flight_code)

        if flight is None:
            print("Booking failed: Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            ticket_count = int(input("Enter number of tickets: "))
        except ValueError:
            print("Booking failed: Age and ticket count must be integers.")
            return

        if passenger_type not in ("regular", "student"):
            print("Booking failed: Choose Regular or Student.")
            return

        if not self.validate_booking(flight, name, age, ticket_count):
            return

        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        self.confirm_booking(flight, passenger, ticket_count)

    # Display the most recent confirmed booking
    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed booking exists yet.")
            return

        self.bookings[-1].display_summary()

    # Main menu
    def run(self):
        print("\nWelcome to Kiran Air Booking!")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("\nThank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


# 7. Program execution
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
