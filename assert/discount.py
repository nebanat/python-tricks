def apply_discount(product, discount):
    """
    simulates creating discount to product prices
    always asserting that discount is > 0 but < product original price

    :param product: product info
    :param discount: discount percentage

    pitfalls of using assertions in Python

    1. Do not use assertions for data validation, since it can be turned on and off
    with the -0 -00 CLI flag or PYTHONOPTIMIZE in CPython

    2. Do not pass a tuple to assertion, because that will never fail, this has to do with
    non-empty tuples always being truthy in Python e.g. assert(1==2, 'This should fail'),
    this is because it asserts the truth value of the tuple instead of asserting the expression

    """
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


if __name__ == '__main__':
    shoes = dict(name='Fancy shoes', price=14900)
    print(apply_discount(shoes, 0.35))
    # print(apply_discount(shoes, 2.0)) this should fail and raise assertion error
