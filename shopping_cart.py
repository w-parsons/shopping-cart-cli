import json
import os
import sys

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


def getItemFromCatalogue(id):
    """
    Utility method to retrieve an item object from the catalogue by its ID.
    """
    for item in Catalogue:
        if item.ID == id:
            return item
    return None


def getID(name):
    """
    Utility method to get the ID of an item, given the name.
    """
    if not isinstance(name, str):
        return -1

    for item in Catalogue:
        if item.Name.strip().lower().replace(" ", "") == name.strip().lower().replace(" ", ""):
            return item.ID
    return -1


def getIDFromIdentifier(identifier, debugPrefix):
    """
    Converts <identifier> into a valid ID
    Returns -1 if identifier is invalid
    """
    if isinstance(identifier, str):
        try:
            id = int(identifier)
            return id
        except:
            id = getID(identifier)
            if id == -1:
                printUsageInformation(debugPrefix + ", invalid identifier")
                return -1
            else:
                return id
    else:
        printUsageInformation(debugPrefix + ", invalid identifier")
        return -1


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


def validateArgs(args, requiredArgCount):
    """
    Makes sure the provided arguments are enough to run a given command,
    prints usage information if not
    """
    if len(args) != requiredArgCount + 2:
        printUsageInformation("Operation failed, invalid arguments")
        exit()


def printUsageInformation(prefix = ""):
    """
    Prints information relating to correct usage.
    """
    s = """
    Shopping List CLI Usage:
        python3 shopping_cart.py <command> <args>
    
    Commands:
        'add' <quantity:int> <name:string>
        'del' <name:string | index:int>
        'set' <quantity:int> <name:string | index:int>
        'list'
    """
    if(prefix != ""):
        print("\n    ====", prefix, "====\n", s)
    else:
        print(s)


def add(quantity, name, cart):
    """
    Adds <quantity> of item with name of <name> to the cart.
    """
    # get item if it is in the catalogue
    item = getItemFromCatalogue(getID(name))

    # ensure quantity is an int and the input item is in the catalogue
    if not isinstance(quantity, int):
        printUsageInformation("Add failed, invalid quantity")
        return
    
    if item is None:
        printUsageInformation("Add failed, could not find item")
        return        
    
    # add item to cart, or increment quantity if already present
    if cart.get(item.ID) == None:
        cart[item.ID] = quantity
    else:
        cart[item.ID] = cart[item.ID] + quantity


def delete(identifier, cart):
    """
    <identifier> can be int (item id) or string (item name).
    Removes the item identified by <identifier> from cart if it is present.
    """
    # get item if it is in the catalogue
    id = getIDFromIdentifier(identifier, "Delete failed")
    if id == -1:
        return
    item = getItemFromCatalogue(id)

    # remove from cart if present
    if item is not None:
        cart.pop(item.ID)
    else:
        printUsageInformation("Delete failed, could not find item")


def set(quantity, identifier, cart):
    """
    <identifier> can be int (item id) or string (item name).
    Sets the quantity of the item identified by <identifier> to <quantity>
    """
    # get item if it is in the catalogue
    id = getIDFromIdentifier(identifier, "Set failed")
    if id == -1:
        return
    item = getItemFromCatalogue(id)

    # ensure quantity is an int and the input item is in the catalogue
    quant = 0
    try:
        quant = int(quantity)
    except:
        printUsageInformation("Set failed, invalid quantity")
        return

    if item is None:
        printUsageInformation("Set failed, could not find item")
        return
    
    # set the item quantity
    cart[item.ID] = quant


def list(cart):
    """
    Prints contents of cart to console.
    """
    table = [["ID", "NAME\t", "COST", "QUANT", "TOTAL_COST"]]
    for id, quantity in cart.items():
        # get item info
        item = getItemFromCatalogue(int(id))
        totalCost = quantity * item.Cost

        # ensure items align correctly
        n = item.Name
        if len(n) < 8:
            n += "\t"

        # create row
        table.append([str(item.ID), n, str(item.Cost), str(quantity), str(totalCost)])
        
    for row in table:
        print('\t'.join(row))


def main():
    # ensure a command has been provided
    args = sys.argv
    if(len(args) < 2):
        printUsageInformation("Operation failed, invalid arguments")
        return
    command = args[1]

    # load current cart state
    cart = load_cart()

    # verify correct num of args provided for given operation, perform operation
    if command == "add":
        validateArgs(args, 2)
        add(int(args[2]), args[3], cart)
    elif command == "del":
        validateArgs(args, 1)
        delete(args[2], cart)
    elif command == "set":
        validateArgs(args, 2)
        set(args[2], args[3], cart)
    elif command == "list":
        validateArgs(args, 0)
        list(cart)
    else:
        printUsageInformation("Operation failed, invalid command")
        return
    
    # once operation is complete, write new cart
    save_cart(cart)


if __name__ == "__main__":
    main()