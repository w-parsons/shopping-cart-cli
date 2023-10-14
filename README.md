# Shopping Cart

This test can be done in the language you are most familiar with. You can choose from:
 - Go
 - Javascript
 - Typescript
 - Python
 - C

## Task Description

You are tasked with implementing basic functionality for a shopping cart system. The system should allow users to add and remove items from their cart, calculate the total price, and apply discounts.

This is a CLI application, please don't implemnt a Web interface/GUI.

The system should expose the following command line actions. Each action should validate the user's inputs before updating a persistent `data.json` file. After processing the action the application should exit.

> Tip: Refer back to this CLI definition often to ensure that your implementation matches the requirements.

```
Shopping Cart CLI

USAGE:
    ./shopping-cart <command>
	
COMMAND:
    add <quantity> "<item>"                 Add a new items with a given quantity. If the item is pre-existing, increment the quantity by <quantity>.
    set <quantity> ["<item>" | <index>]     Update the given item quantity.
    del ["<item>" | <index>]                Delete a given item by name or index.
    list                                    List all items with their indexes, quantity, unit cost, and total cost.
```

The `data.json` format is up to you, but an easy example could be -

```
{
    "items": [
        {"name": "<item>", "quantity": <quantity>},
        ...
    ]
}
```

## Products

The shopping cart will be required to store information about what products are in it.

A product has a name and a price. For example, this could be the following.

| Product   | Price |
| --------  | ----- |
| Wall Art  | 10.99 |
| Rug       | 120   |
| Coat Rack | 9.99  |
| Clock     | 5     |
| Couch     | 1000  |

> Note: These products are hard coded into the starter application.


## Main Task 

Implement the commands to the following specifications.

> Tip: Focus on implementing the `add` and `del` commands first, then `list` and `set`.

For `add` -

- Validate that `<quantity>` is a number.
- Validate that `<item>` is a string, and is in the catalogue.
- If valid, add the new item to the cart, and save the updated cart to `data.json`.

An example is:

```
./shopping-cart add 2 "Rug"
```

For `del` -

- Validate that `["<item>" | <index>]` can be mapped to a valid item in the cart, either by index or item name.
- If valid, delete the item from the cart, and save the updated cart to `data.json`.

An example is:

```
./shopping-cart del "Rug"
```

For `set` -

- Validate that `["<item>" | <index>]` can be mapped to a valid item in the cart, either by index or item name.
- If valid, update the item in the cart, and save the updated cart to `data.json`.

An example is:

```
./shopping-cart set 1 "Rug"
```

For `list` -

- List all items in the cart with their indexes, quantity, unit cost, and total cost.

## Bonus Task - Discounts

We would like to be able to give out discount codes.

The code for the shopping cart must be able to do the following:
 - Apply a discount to all products in the cart.
 - Apply a discount to a specific product in the cart.

Add the following discount codes into the application -

| Code      | Discount | Items       |
| --------  | -------- | ----------- |
| SAVE50    | 50%      | All         |
| RUG30     | 30%      | `Rug`       |
| COATS     | 99%      | `Coat Rack` |

Add a new `discount` command with the following options -

```
./shopping-cart discount <code> ["<item>" | <index>]
```

- Validate that `<code>` is a valid code.
- Validate that `["<item>" | <index>]` can be mapped to a valid item in the cart, either by index or item name.
- If valid, update the cost of the items in the cart, and save the updated cart to `data.json`.

## Bonus Task - Tax

We would like to be able to show customers the cost of their cart with inclusive and exclusive of tax:

The code for the shopping cart must be able to do the following:
 - Get the total cost of the shopping cart tax exclusive (you may assume that the prices of the products are always tax exclusive)
 - Get the total cost of the shopping cart tax inclusive. (you may assume the tax applied is NZ GST of 15%)

## Bonus Task - Tests

Add some test cases to validate your code. This could be manual test cases that you are running, unit tests to validate your input parsing or another form of test that is easily repeatable.