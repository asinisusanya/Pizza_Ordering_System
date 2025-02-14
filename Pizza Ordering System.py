def display_pizza_menu():
    print("\n------Pizza Prices------")
    for i, (name, price) in enumerate(pizza_menu.items(), 1):
        print(f"{i}. {name:<15} {price:.2f}")
    print("---------------------------")


def display_topping_menu():
    print("\n------Topping Prices------")
    for i, (name, price) in enumerate(topping_menu.items(), 1):
        print(f"{i}. {name:<15} {price:.2f}")
    print("---------------------------")


def order_pizza():
    customer = {
        'name': input("Insert Name: "),
        'id': input("Insert National ID: "),
        'phone': input("Insert Mobile Number: ")
    }

    num_pizzas = int(input("Enter number of pizzas: "))
    order = []
    total = 0

    for _ in range(num_pizzas):
        display_pizza_menu()
        pizza_choice = int(input("Select your pizza: ")) - 1
        pizza_name = list(pizza_menu.keys())[pizza_choice]
        pizza_price = pizza_menu[pizza_name]

        display_topping_menu()
        topping_choice = int(input("Select your topping: ")) - 1
        topping_name = list(topping_menu.keys())[topping_choice]
        topping_price = topping_menu[topping_name]

        quantity = int(input("Input pizza quantity: "))
        size_choice = int(input("-----Select Pizza Size------\n1. Regular\n2. Large\nSelect your choice: "))

        if size_choice == 2:
            pizza_price += 250

        total_price = (pizza_price + topping_price) * quantity
        order.append((pizza_name, topping_name, size_choice, quantity, total_price))
        total += total_price

    print_receipt(customer, order, total)


def print_receipt(customer, order, total):
    print("\n----------Order Details---------")
    print(f"Customer Name  : {customer['name']}")
    print(f"Customer ID    : {customer['id']}")
    print(f"Customer Phone : {customer['phone']}")
    for item in order:
        size = "Large" if item[2] == 2 else "Regular"
        print(f"{size} {item[0]} - {item[1]} {item[3]} → {item[4]:.2f}")
    print(f"TOTAL → {total:.2f}")
    print("---------Thank you------")


def main():
    while True:
        print("\n------Pizza Store Menu------")
        print("1. Order Pizza")
        print("2. View Pizza Menu")
        print("3. View Toppings Menu")
        print("9. Exit")
        choice = int(input("Your Selection: "))

        if choice == 1:
            order_pizza()
        elif choice == 2:
            display_pizza_menu()
        elif choice == 3:
            display_topping_menu()
        elif choice == 9:
            print("Thank you for visiting our Pizza Store!")
            break
        else:
            print("Invalid choice, please try again.")


pizza_menu = {
    "Hot & Spicy": 500.00,
    "Cheesy": 650.00,
    "Veggie": 500.00,
    "Meat": 700.00,
    "BBQ Chicken": 750.00
}

topping_menu = {
    "Pepperoni": 100.00,
    "Mushroom": 150.00,
    "Extra cheese": 200.00,
    "Onion": 150.00,
    "Green pepper": 100.00
}

if __name__ == "__main__":
    main()