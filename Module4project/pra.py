import time

class DunnDelivery:
    def __init__(self):
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    def show_menu(self):
        print("\n==== MENU ====")
        for category, items in self.menu.items():
            print(f"\n=== {category} ===")
            for item in items:
                print(f"{item}: ${self.prices[item]:.2f}")

    def calculate_total(self, items, has_student_id=False):
        total = sum(self.prices[item] for item in items)
        if has_student_id and total > 10:
            total *= 0.9
        return total

    def estimate_delivery(self, location, current_hour):
        base_time = self.delivery_locations.get(location, 10)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        return base_time

    def print_order(self, location, items, current_hour, has_student_id=False):
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        total = self.calculate_total(items, has_student_id)
        delivery_time = self.estimate_delivery(location, current_hour)

        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        if has_student_id:
            print("Student discount applied!")
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")
        return delivery_time  # Return the delivery time to use later

def main():
    delivery = DunnDelivery()
    delivery.show_menu()
    print()

    order = []
    while True:
        item = input("Enter item to order (or 'done' to finish): ").strip().lower()  # Convert to lowercase
        if item == 'done':
            break
        # Check if item is valid (case-insensitive)
        if any(item == menu_item.lower() for sublist in delivery.menu.values() for menu_item in sublist):  
            order.append(item.capitalize())  # Capitalize to match the format of the menu
        else:
            print("Item not found in menu. Please try again.")

    if not order:
        print("No items selected. Exiting.")
        return

    print("\nDelivery Locations:")
    for loc in delivery.delivery_locations.keys():
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
    estimated_time = time.strftime("%I:%M %p", time.localtime(time.mktime(time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, delivery_hour, delivery_minute, 0, 0, 0, -1)))))
    
    print(f"Your order will be there at: {estimated_time}")

if __name__ == "__main__":
    main()
