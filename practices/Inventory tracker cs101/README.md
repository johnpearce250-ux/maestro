# Inventory Tracker (CS101)

A simple command-line inventory tracker written in Python. It supports adding items, removing items, viewing current inventory, and assigning SKUs to new items.

## Features

- Add stock to existing items
- Add new items and auto-assign a new SKU
- Remove stock with insufficient-inventory checks
- Show current inventory from an interactive menu
- Quit safely from the program loop

## Project Files

- `inventory_tracker.py` — Main runnable Python script
- `inventory_tracker.md` — Markdown documentation with code snapshot
- `Pseudo.py` — Pseudocode version of the inventory flow

## Requirements

- Python 3.8+

## How to Run

1. Open a terminal in this project folder.
2. Run:

```bash
python inventory_tracker.py
```

## Menu Options

- `add` — Add an amount to an item
- `remove` — Remove an amount from an item
- `show` — Display all inventory items and amounts
- `quit` — Exit the tracker

## Example Flow

1. Start the app
2. Enter `add`, provide item name and amount
3. Enter `show` to verify changes
4. Enter `remove` to reduce stock
5. Enter `quit` to exit

## Notes

- If you add an item that is not in the SKU dictionary, a new SKU is created automatically.
- If you try to remove more than available stock, the program warns and skips the update.

## Future Improvements

- Save and load inventory data from a file (JSON/CSV) so data persists between runs
- Prevent negative amounts for add/remove operations
- Add confirmation messages after successful add/remove actions
- Display SKU values in the `show` output
- Add unit tests for add/remove logic and edge cases
