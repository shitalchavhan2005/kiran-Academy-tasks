
import random

# Predefined cab types and rates
cab_rates = {
    "1": ("Auto", 12),
    "2": ("Sedan", 18),
    "3": ("SUV", 25)
}

# Predefined routes and distances
routes = {
    "1": ("Pune Station", "Shivajinagar", 5),
    "2": ("Swargate", "Kothrud", 8),
    "3": ("Hinjawadi", "Wakad", 10)
}

# Main menu loop
while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    # Exit option
    if choice == "2":
        print("\nThank you for using our Cab Booking Chatbot!")
        print("Goodbye!")
        break

    # Book ride option
    elif choice == "1":
        print("\n---------- Choose Cab Type ----------")
        print("1. Auto  - Rs. 12/km")
        print("2. Sedan - Rs. 18/km")
        print("3. SUV   - Rs. 25/km")

        cab_choice = input("Select cab type: ").strip()

        if cab_choice not in cab_rates:
            print("Invalid cab choice. Returning to main menu.")
            continue

        cab_name, rate = cab_rates[cab_choice]

        # Display predefined routes
        print("\n---------- Choose Route ----------")
        print("1. Pune Station -> Shivajinagar (5 km)")
        print("2. Swargate -> Kothrud (8 km)")
        print("3. Hinjawadi -> Wakad (10 km)")

        route_choice = input("Select route: ").strip()

        if route_choice not in routes:
            print("Invalid route choice. Returning to main menu.")
            continue

        source, destination, distance = routes[route_choice]

        # Calculate fare
        fare = rate * distance

        print("\n========== RIDE DETAILS ==========")
        print("Cab Type       :", cab_name)
        print("Source         :", source)
        print("Destination    :", destination)
        print("Distance       :", distance, "km")
        print("Rate per km    : Rs.", rate)
        print("Total Fare     : Rs.", fare)

        # Confirm or cancel before OTP sharing
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm_choice = input("Enter your choice: ").strip()

        if confirm_choice == "2":
            print("\nRide cancelled successfully.")
            print("No OTP has been shared.")
            print("Returning to main menu.")
            continue

        elif confirm_choice == "1":
            # Generate a four-digit OTP
            otp = random.randint(1000, 9999)

            print("\nYour ride OTP is:", otp)
            print("OTP has been shared with the user.")
            print("IMPORTANT: Once the OTP is shared,")
            print("the ride cannot be cancelled.")
            print("Booking confirmed successfully!")

        else:
            print("Invalid confirmation choice.")
            print("No OTP has been shared.")
            print("Returning to main menu.")
            continue

    else:
        print("Invalid menu choice. Please select 1 or 2.")
