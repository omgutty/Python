# This program shows divmod(), multiple assignment, and += / -= shortcuts.
# divmod(a, b) gives back two values: the quotient and the remainder.

# 5 divided by 2 -> quotient 2 (q), remainder 1 (r)
q, r = divmod(5, 2)
print(q)
print(r)


# Assign three values to three variables in one line.
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Increment (++) / Decrement (--) Operators
# Good news - Doesn't have ++, -- operator

x = 5
# += is a shortcut: x += 1 means x = x + 1, so x becomes 6.
x += 1
print(x)

# -= is a shortcut: x -= 1 means x = x - 1, so x becomes 5.
x -= 1  # x= x-1
print(x)

# *= is a shortcut: x *= 3 means x = x * 3, so x becomes 15.
x *= 3  # x= x*1
print(x)