"""
🛒 Simple Shopping Cart
Add items + prices
Show total bill

👉 Skills:

lists/dictionaries
loops
sum logic

"""

cart = {}

while True:
    print("\n🛒 Shopping Cart")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart[item] = price
        print(f"{item} added successfully.")

    elif choice == "2":
        if not cart:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for item, price in cart.items():
                print(f"{item}: ${price}")

    elif choice == "3":
        total = sum(cart.values())
        print(f"\nTotal Bill: ${total}")

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")