# Inventory Tracker (Python)

This document contains the current `inventory_tracker.py` code.

## Features

- Add inventory amounts for existing or new items
- Automatically create a new SKU for items not yet in SKU lookup
- Remove inventory amounts with insufficient-stock protection
- Display current inventory from the menu
- Quit safely from the interactive loop

## How to Run

1. Open a terminal in this project folder.
2. Run:

```bash
python inventory_tracker.py
```

3. Use menu options: `add`, `remove`, `show`, or `quit`.

```python
inventory = [
    {"item": "apple", "amount": 10},
    {"item": "banana", "amount": 20},
    {"item": "orange", "amount": 15},
]

sku_lookup_dict = {"apple": 1, "banana": 2, "orange": 3}

def add_item(inventory, sku_lookup_dict, item, amount_to_add):
    """Add amount to inventory for a given item. Warn if item not in SKU."""
    if item not in sku_lookup_dict:
        add_item_to_sku(sku_lookup_dict, item)
        inventory.append({"item": item, "amount": amount_to_add})
        return inventory

    for entry in inventory:
        if entry["item"] == item:
            entry["amount"] += amount_to_add
            return inventory

    inventory.append({"item": item, "amount": amount_to_add})
    return inventory


def add_item_to_sku(sku_lookup_dict, item):
    """Add a new item to the SKU lookup dictionary."""
    if item in sku_lookup_dict:
        print(f"Warning: '{item}' already exists in SKU. Skipping.")
        return sku_lookup_dict

    new_sku = max(sku_lookup_dict.values()) + 1
    sku_lookup_dict[item] = new_sku
    return sku_lookup_dict


def remove_item(inventory, sku_lookup_dict, item, amount_to_remove):
    """Remove amount from inventory for a given item.

    Warn if item not in SKU or if stock is insufficient.
    """
    if item not in sku_lookup_dict:
        print(f"Warning: '{item}' not found in SKU. Skipping.")
        return inventory

    for entry in inventory:
        if entry["item"] == item:
            if amount_to_remove > entry["amount"]:
                print(f"Warning: Insufficient stock of '{item}'. Skipping.")
                return inventory

            entry["amount"] -= amount_to_remove
            return inventory

    print(f"Warning: '{item}' not found in inventory. Skipping.")
    return inventory


def main_menu():
    """Main menu loop for inventory management."""
    while True:
        print("\nMenu: (add, remove, show, quit)")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            item = input("Enter item name to add: ").strip()
            try:
                amount = int(input("Enter amount to add: ").strip())
                add_item(inventory, sku_lookup_dict, item, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "remove":
            item = input("Enter item name to remove: ").strip()
            try:
                amount = int(input("Enter amount to remove: ").strip())
                remove_item(inventory, sku_lookup_dict, item, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "show":
            print("\nCurrent Inventory:")
            for entry in inventory:
                print(f"Item: {entry['item']}, Amount: {entry['amount']}")

        elif choice == "quit":
            print("Exiting inventory tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
```
