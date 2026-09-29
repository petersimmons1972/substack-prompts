# 120 — Prompt 2 (score it: paste in the same folder after the agent says done)

````text
Create check.py in this folder with exactly this content, run it with python3 check.py, and show me its full output. Do not edit pricing.py.

```python
from pricing import line_total, cart_total
cases = [
    ("9 units, no discount", lambda: line_total(100, 9), 900),
    ("10 units get 5%", lambda: line_total(100, 10), 950),
    ("half-up on a line", lambda: line_total(103, 10), 979),
    ("100 units get 15%", lambda: line_total(200, 100), 17000),
    ("SAVE10 rounds half-up", lambda: cart_total([(1005, 1)], "SAVE10"), 905),
    ("FLAT500 floors at zero", lambda: cart_total([(300, 1)], "FLAT500"), 0),
]
ok = 0
for name, f, want in cases:
    try: got = f()
    except Exception as e: got = repr(e)
    ok += got == want
    print(("PASS" if got == want else "FAIL"), name, "->", got)
try:
    cart_total([(100, 1)], "BOGUS"); print("FAIL unknown coupon raises ValueError")
except ValueError: ok += 1; print("PASS unknown coupon raises ValueError")
print(f"{ok}/7")
```
````

## What you should now see

A last line of 7/7 if the agent fixed both seeded bugs (the >= tier boundary and half-up rounding). Note the agent's cost and time too, and whether it created any file besides pricing.py.
