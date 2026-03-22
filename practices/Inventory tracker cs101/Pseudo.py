Load inventory and SKU data

while True:
	Show menu: (add, remove, show, quit)
	Get user choice

	if choice == "add":
		Ask for item name and amount
		if item not in SKU:
			Warn and skip
		else:
			Add amount (update inventory)

	elif choice == "remove":
		Ask for item name and amount
		if item not in SKU:
			Warn and skip
		elif amount > stock:
			Warn and skip
		else:
			Subtract amount

	elif choice == "show":
		Display all inventory (item, SKU, amount)

	elif choice == "quit":
		break

Save or print final inventory