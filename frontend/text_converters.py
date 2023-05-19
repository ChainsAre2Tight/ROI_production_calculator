from backend.factory import FactoryInterface
from backend.product import ProductInterface


def convert_requirements_to_output_format(req: dict) -> str:
    result = '\n'.join(
        [
            f'{product.product_type}: {amount}' for product, amount in req.items()
        ]
    )
    return result


def convert_factories_to_output_format(req: dict) -> str:
    result = '\n'.join(
        [
            factory.name + '\n' + '\n'.join(
                [
                    f'---> {product.product_type}: {amount}'
                    for product, amount in products.items()
                ]
            )
            for factory, products in req.items()
        ]
    )
    return result
