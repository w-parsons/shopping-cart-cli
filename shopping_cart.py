import json
import os

class Cart:
    print()
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

def getID(name):
    """
    Utility method to get the ID of an item, given the name.
    """

    for item in Catalogue:
        if item.Name == name:
            return item.ID
    return -1

def getName(id):
    """
    Utility method to get the name of an item, given the ID.
    """

    for item in Catalogue:
        if item.ID == id:
            return item.Name
    return None

def debugCart(cart):
    """
    Utility method to print the current contents of the cart.
    """
        
    for k, v in cart.items():
        print(k, getName(k), v)

def load_cart():
    """
    Loads cart data from 'data.json' and returns it as a Dictionary where
    the key is the item ID, and the value is the item quantity
    """

    path = 'data.json'
    if not os.path.exists(path):
        return
    file = open(path)
    data = json.load(file)

    result = {}
    for item in data:
        result[int(item['id'])] = int(item['quantity'])

    return result

def save_cart(cart):
    """
    Saves the contents of the cart to data.json
    """

    items = []
    for k, v in cart.items():
        items.append(
            {
                "id": k,
                "quantity": v
            }
        )
    obj = json.dumps(items, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(obj)

def main():
    cart = load_cart()
    save_cart(cart)

if __name__ == "__main__":
    main()