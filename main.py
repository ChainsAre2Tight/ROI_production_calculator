from product import Product


def dict_keys_to_string(d: dict):
    for key in list(d.keys()):
        d[key.product_type] = d.pop(key)
    return d


def get_requirements_of_a_product(product: Product, amount: int = 1) -> dict:
    requirements = dict()
    product.get_requirements(
        target=requirements,
        amount=amount,
        include=False,
    )
    return requirements


if __name__ == '__main__':
    from info import pizza
    print(dict_keys_to_string(get_requirements_of_a_product(pizza, 1)))
