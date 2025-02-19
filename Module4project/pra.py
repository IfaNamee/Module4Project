# Name: Ifa Namee
# Class: Capstone project
# Date: 2/17/2025
# description: The DunnDelivery class demostrates core OOP concepts

# Note
# - Encapsulation: Data (menu and prices) and methods are bundled in the class.
# - Abstraction: Complex delivery logic is hidden behind simple method calls.

import time

class DunnDelivery:
    # Constructor method - creates a new instance of a delivery
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Mocha", "Macchiato", "Caramel"], # add three drinks
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Prices encapsulated within the class with add three coffee with prices
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99, "Mocha": 5.99, "Macchiato": 5.49, "Caramel": 4.50,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    # Show the menu of items available for delivery
    def show_menu(self):
        print("\n==== MENU ====")
        # Show the menu items for the chosen category
        for category, items in self.menu.items():
            print(f"\n=== {category} ===")
            for item in items:
                print(f"{item}: ${self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False, priority_input="no"):
        # Calculate the sum of item prices
        total = sum(self.prices[item] for item in items)

        # Add $2 for priority delivery if selected
        if priority_input == "yes":
            total += 2  # Add $2 for priority delivery
        
        if has_student_id and total > 10:
            total *= 0.9  # Apply discount directly without adding $2

        return total  # Return the final total cost


    # Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour):
        # Ask the user if they want priority delivery
        priority_input = input("Do you want priority delivery? 2 dollors extra and 3 mins fast (yes/no): ").strip().lower()
    
        # Get the base delivery time for the location, defaulting to 10 minutes if not found
        base_time = self.delivery_locations.get(location, 10)

        # Check if it's during peak hours
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5

        # Handle priority delivery
        if priority_input == "yes":
            # Reduce the time by 3 minutes for priority delivery
            base_time = max(0, base_time - 3)  # Ensure time doesn't go below 0 minutes
        elif priority_input not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            priority_input = "no"

        # Return the final estimated delivery time
        return base_time, priority_input


    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False):
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        delivery_time, priority_input = self.estimate_delivery(location, current_hour)
        total = self.calculate_total(items, has_student_id, priority_input)

        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        
        # print only if priority delivery is selected 
        if priority_input == "yes":
            print("Priority delivery fee: $2.00")

        # if ststement only if user is student and total order more than 10
        if has_student_id and total > 10: 
            print("Student discount applied!")
            print(f"Total after discount: ${total:.2f}")
        else: # If no discount is applied
            print(f"Total amount: ${total:.2f}")  
        print(f"Estimated delivery time: {delivery_time} minutes")
        return delivery_time  # Return the delivery time to use later
    
    # Rate method that lets customers rate their delivery.
    def rate_delivery(self):
        try:
            rate = int(input("Rate our delivery (1-5 stars): "))
            if 1 <= rate <= 5:
                return rate
            else:
                print("Invalid rating. Please enter a number between 1 and 5.")
                return self.rate_delivery()  # return to ask again
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.rate_delivery()  # return to ask again

    # Comment method. Ask user if they want to leave a comment.  
    def comment(self):
        choice = input("Would you like to add a comment about your experience? (yes/no): ").strip().lower()
        if choice == "yes":
            comments = input("How is your experience with Dunn Brothers delivery? ").strip()
            if comments:  # Ensures the input is not empty
                print()
                print("Cusromer feedback:", comments)
                print("Thank You! for the feedback!")

# main method is executed as soon as the program runs
def main():
    delivery = DunnDelivery()
    delivery.show_menu()
    print()

    order = []
    while True: # Ask user to enter orders or finish
        item = input("Enter item to order (or 'done' to finish): ").strip().lower()  # Convert to lowercase
        if item == 'done':
            break
        # Check if item is valid (case-insensitive)
        found = False
        for category, items in delivery.menu.items():
            for menu_item in items:
                if item == menu_item.lower():  # Compare in lowercase
                    order.append(menu_item)  # Add the correct capitalized menu item
                    found = True
                    break
            if found:
                break
        if not found:
            print("Item not found in menu. Please try again.")

    if not order:
        print("No items selected. Exiting.")
        return

    print("\nDelivery Locations:")
    for loc in delivery.delivery_locations.keys(): # It same us menu handle use short cut keys
        print(f"- {loc}")
    print()

    while True: 
        location = input("Enter delivery location: ").strip().lower()  # Convert to lowercase
        # Check if location is valid (case-insensitive)
        if location.lower() in [loc.lower() for loc in delivery.delivery_locations]:
            # Find exact location name to match format
            location = next(loc for loc in delivery.delivery_locations if loc.lower() == location)
            break
        print("Invalid location. Please enter a valid location.")

    student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == 'yes'

    # Get current time automatically using time.localtime()
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    # Print order details
    delivery_time = delivery.print_order(location, order, current_hour, has_student_id=student_id)

    # Format current time (12-hour format with AM/PM)
    formatted_time = time.strftime("%I:%M %p", current_time)
    formatted_date = time.strftime("%m-%d-%Y", current_time)  # Format date (MM-DD-YYYY)
    print(f"Current time is: {formatted_time}, {formatted_date}")

    # Calculate estimated delivery time
    total_minutes = current_hour * 60 + current_minute + delivery_time  # Convert to total minutes
    delivery_hour = (total_minutes // 60) % 24  # Get the hour part, ensure it wraps around 24
    delivery_minute = total_minutes % 60  # Get the minute part

    # Format the estimated time in 12-hour format with AM/PM
    estimated_time = time.strftime("%I:%M %p", time.localtime(time.mktime(time.struct_time(
        (current_time.tm_year, current_time.tm_mon, current_time.tm_mday, delivery_hour, delivery_minute, 0, 0, 0, -1)))))
    
    print(f"Your order will be there at: {estimated_time}")

    print()
    delivery.rate_delivery()  # Print out delivery rate
    delivery.comment()  # Print out comment

if __name__ == "__main__":
    main()
