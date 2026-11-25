# Full code: Agentic Coding Explained: How AI Coding Agents Plan, Edit and Check Your Code

The practice code and its test from this video: made-up Test Bakery cake orders, with one bug on purpose for a coding agent to find. Written for this video and not run for it (docs only); traced by hand: before the fix the test stops with "expected 128, got 86", and after it prints "Test passed: 128 cake orders". Needs Python 3.

### cake_orders.py
```
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
```

### test_cake_orders.py
```
# test_cake_orders.py: checks that total_orders adds up the made-up Test Bakery orders.
# Save it the same way, as test_cake_orders.py, in the same folder as cake_orders.py.
# Run it in a terminal opened in that folder: python test_cake_orders.py
# (on Windows, if python isn't found, try: py test_cake_orders.py)

from cake_orders import total_orders

total = total_orders([42, 35, 51])
assert total == 128, f"expected 128, got {total}"
print("Test passed: 128 cake orders")
```

### The fix (for checking your agent's work)
```
# In cake_orders.py, the loop starts at the second order, so the first one (42) is skipped.
# The one-line fix, shown as the old line (minus) and the new line (plus):
-    for count in orders[1:]:
+    for count in orders:
```
