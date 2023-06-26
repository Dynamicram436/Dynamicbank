from datetime import datetime

def generate_bill():
    # List of items with prices
    items = {
        'rice': 55,
        'sugar': 44,
        'Krystal salt': 22,
        'palm oil': 150,
        'panner': 220,
        'mushroom': 300,
        'boost': 200,
        'pepsodent': 50
    }

    # Prompt for customer name
    name = input("Enter your name: ")

    # Initialize variables
    total_price = 0
    purchased_items = []

    # Purchase loop
    while True:
        print("Available Items:")
        for item, price in items.items():
            print(f"{item}: Rs {price}")

        item = input("Enter the item you want to buy (or 'done' to finish): ")

        if item.lower() == 'done':
            break

        if item in items:
            quantity = int(input("Enter the quantity: "))
            price = items[item] * quantity
            purchased_items.append((item, quantity, price))
            total_price += price
        else:
            print("Invalid item. Please try again.")

    # Calculate GST and final amount
    gst = (total_price * 5) / 100
    final_amount = total_price + gst

    # Print the bill
    print("\n" + "=" * 30 + " Supermarket Bill " + "=" * 30)
    print("Customer Name:", name)
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 75)
    print("Item\t\tQuantity\tPrice")
    print("-" * 75)
    for i, (item, quantity, price) in enumerate(purchased_items, start=1):
        print(f"{i}. {item}\t\t{quantity}\t\tRs {price}")
    print("-" * 75)
    print(f"Total Amount:\t\t\t\tRs {total_price}")
    print(f"GST (5%):\t\t\t\tRs {gst}")
    print("-" * 75)
    print(f"Final Amount:\t\t\t\tRs {final_amount}")
    print("-" * 75)
    print("Thank you for shopping with us!")

# Main program
generate_bill()
