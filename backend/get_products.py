import backend.information.products


def get_product_names() -> list:
    return [item for item in dir(backend.information.products) if
            not item.startswith("__") and item not in ['Product', 'factories']]


def get_products() -> dict:
    names = get_product_names()
    prod = dict()
    for product_name in names:
        prod[product_name] = eval(f'backend.information.products.{product_name}')

    return prod


if __name__ == "__main__":
    print(get_products())
