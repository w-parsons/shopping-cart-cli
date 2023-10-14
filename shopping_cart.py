class Cart:
    # TODO: Implement the cart class


class Item:
    def __init__(self, ID, Name, Cost):
        self.ID = ID
        self.Name = Name
        self.Cost = Cost

Catalogue = [
    Item(1, "Wall Art", 10.99),
    Item(2, "Rug", 120.00),
    Item(3, "Coat Rack", 9.99),
    Item(4, "Clock", 5.00),
    Item(5, "Couch", 1000.00)
]

def load_cart():
    # TODO: Implement loading the cart from ./data.json. If the file is missing, return an empty cart.
    return None

def save_cart(cart):
    # TODO: Implement save a cart to ./data.json.
    return None

def main():
    cart = load_cart()

if __name__ == "__main__":
    main()