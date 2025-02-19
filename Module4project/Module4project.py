# Name: Ifa Namee
# Class: Capstone project
# Date: 2/7/2025
# description: The DunnDelivery class demostrates core OOP concepts

# Note
# - Encapsulation: Data (menu and prices) and methods are bundled in the class.
# - Abstraction: Complex delivery logic is hidden behind simple method calls.

class DunnDelivery:
    # Constructor method - creates a new instance of a delivery 
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuchino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]             
        }

        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuchino": 4.99,
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
    def show_menu(self, category=None):
        if category:
            #Show the menu items for the chosen category
            print(f"\n=== {category} ===")
            # Loop through the items in that specific category on the menu
            # and display them to the user
            for item in self.menu[category]:
                 print(f"{item}: ${self.prices[item]:.2f}")
        else:
        #Show the entire menu
            for category in self.menu: # First show the category name
                print(f"\n==== {category} ====")
            # Second show the items within the category
            for item in self.menu[category]:
                  print(f"{item}: ${self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False):
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        #Calcaulte the student discount based on the student id
        if has_student_id and total > 10:
            total *= 0.9

        # This method returns the total cost of the order to the code that
        # called the method
        return total;

    # Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour):
        # Calculate the base time
        base_time = self.delivery_locations[location]

        # Calculate the delivery time based on the time of day (adjust for busy times of day)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
     
        #If they aren't ordering during a busy time, return the base time with no adjustment
        return base_time

    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False):
        # Display the order information
        print("\n=== Order Summary===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")
    
        # Loop through the list of menu items they ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # Call the methods to get the total cost and the delivery time
        total = self.calculate_total(items, has_student_id);
        delivery_time = self.estimate_delivery(location, current_hour)

        # Display the subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        # Calculate the total with the discount if the customer has a student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied!")

        # display total after discount & estimated delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

# main method is executed as soon as the program runs
def main():
    #Create a new delivery object - instantiating a new object
    delivery = DunnDelivery()

    # Show menu
    delivery.show_menu("Coffee Drinks")

    # Sample order at 9:30 AM (peak morning hour)
    order = ["Latte", "Bagel", "Chicken Wrap"]

    # Display receipt for the order
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True);

# Add the line of code to automatically call the main method
if __name__ == "__main__":
    main()