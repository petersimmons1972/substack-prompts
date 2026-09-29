In this empty folder, create pricing.py with exactly this content:

```python
# Pricing rules (this is the spec):
# 1. Prices are integer cents. Round every total half-up to a whole cent.
# 2. Bulk discount per line: 5% at 10 or more units, 10% at 50+, 15% at 100+.
# 3. Coupons apply to the cart total after bulk discounts.
#    SAVE10 takes 10% off. FLAT500 takes 500 cents off, never below zero.
#    An unknown coupon raises ValueError.

TIERS = [(10, 0.05), (50, 0.10), (100, 0.15)]

def line_total(unit_cents, qty):
    rate = 0
    for min_qty, r in TIERS:
        if qty > min_qty:
            rate = r
    return round(unit_cents * qty * (1 - rate))
```

Then add cart_total(lines, coupon=None), where lines is a list of (unit_cents, qty) pairs, and make sure the whole module follows the pricing rules at the top of the file. Only edit pricing.py. Tell me when you are done.
