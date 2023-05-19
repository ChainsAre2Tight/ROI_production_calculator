from backend.product import Product


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
    from backend.information.products import pizza

    # print(dict_keys_to_string(get_requirements_of_a_product(pizza, 1)))


def factories_from_demand(
        product: Product,
        required: int,
        per: int,
) -> dict:
    requirements = product.get_requirements(amount=required)
    required_factories = dict()
    for product, amount in requirements.items():
        required_per_day = amount / per
        produced_per_day = product.amount_produced / product.production_time
        num_required_factories = required_per_day / produced_per_day

        factory = product.production_facility
        if factory not in required_factories.keys():
            required_factories[factory] = dict()
        required_factories[factory][product] = num_required_factories

    return required_factories


def factories_to_str(f: dict):
    for key in list(f.keys()):
        f[key.name] = dict_keys_to_string(f.pop(key))
    return f


def stringified_factories_from_demand(
        product: Product,
        required: int,
        per: int,
) -> dict:
    return factories_to_str(
        factories_from_demand(
            product=product,
            required=required,
            per=per,
        )
    )


def stringified_product_requirements(
        product: Product,
        amount: int = 1,
) -> dict:
    return dict_keys_to_string(
        get_requirements_of_a_product(
            product=product,
            amount=amount,
        )
    )


if __name__ == '__main__':
    from backend.information.products import leather

    print(factories_to_str(
        factories_from_demand(leather, 7, 15))
    )
    print(factories_to_str(
        factories_from_demand(pizza, 9, 15))
    )
