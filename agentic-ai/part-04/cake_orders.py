# cake_orders.py: adds up a day's cake orders for Test Bakery, a made-up shop.
# Practice code for Agentic AI, Part 4: it has one bug in it, on purpose.
# To keep a copy: paste this into Notepad and save it as cake_orders.py, with the box called
# Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.
# Save it in a new, empty folder, next to test_cake_orders.py.

def total_orders(orders):
    total = 0
    for count in orders[1:]:
        total += count
    return total
