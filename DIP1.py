class Menu:
    def __init__(self):
        self.menu = {'Spaghetti': 10, 'Burger': 8, 'Pizza': 12}
        self.order = {}

    def show_menu(self):
        print("Welcome to our restaurant! Here's our menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def order_food(self):
        while True:
            food = input("What would you like to order? (or type 'exit' to finish) ")
            if food.lower() == 'exit':
                break
            elif food not in self.menu:
                print("Sorry, we don't have that. Please order something from the menu.")
            else:
                while True:
                    try:
                        quantity = int(input("How many would you like to order? "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                if food in self.order:
                    self.order[food] += quantity
                else:
                    self.order[food] = quantity
                print(f"You've ordered {self.order[food]} {food}(s).")

    def calculate_total(self):
        total = 0
        print("You've ordered:")
        for item, quantity in self.order.items():
            print(f"{item}: {quantity}")
            total += self.menu[item] * quantity
        print(f"Your total bill is: ${total:.2f}")


# Run the program
restaurant = Menu()
restaurant.show_menu()
restaurant.order_food()
restaurant.calculate_total()
