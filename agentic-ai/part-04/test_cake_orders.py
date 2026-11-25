# test_cake_orders.py: checks that total_orders adds up the made-up Test Bakery orders.
# Save it the same way, as test_cake_orders.py, in the same folder as cake_orders.py.
# Run it in a terminal opened in that folder: python test_cake_orders.py
# (on Windows, if python isn't found, try: py test_cake_orders.py)

from cake_orders import total_orders

total = total_orders([42, 35, 51])
assert total == 128, f"expected 128, got {total}"
print("Test passed: 128 cake orders")
