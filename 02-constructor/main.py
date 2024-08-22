class Item:
    """
    Item class to represent an item with a name, price and quantity.
    """
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'price {price} is not greater than zero!'
        assert quantity >= 0, f'quantity {quantity} is not greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


# Instance of class Item
item1 = Item("Phone", 1000, 1)
item2 = Item("Laptop", 10000, 3)

# Print Item
print(item1.calculate_total_price())
print(item2.calculate_total_price())
