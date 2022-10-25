# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# : Replace temporary variable with extracted method/query

# Code snippet. Not runnable.

from email.charset import BASE64


def discount_factor(base_price):
    if base_price > 1000:
        return 0.95
    else:
        return 0.908

def get_price(quantity, item_price):
    base_price = quantity * item_price
    discount = discount_factor(base_price)
    return base_price * discount
