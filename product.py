from abc import ABC, abstractmethod


class ProductInterface(ABC):
    product_type: str
    production_time: int
    requirements: dict | None
    amount_produced: int

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def produced_per_day(self):
        pass

    @property
    @abstractmethod
    def required_per_day(self):
        pass

    @abstractmethod
    def _get_requirements(self, target: dict | None = None, amount: int = 1, red: int = 1) -> dict:
        pass


class Product(ProductInterface):

    def __init__(self, product_type: str, production_time: int, amount_produced: int,
                 requirements: dict | None):
        self.product_type = product_type
        self.production_time = production_time
        self.amount_produced = amount_produced
        self.requirements = requirements

    def __str__(self):
        return f'''Product "{self.product_type}" takes {self.production_time} days to produce and requires {
        ', '.join([f'{product.product_type} x {amount}' for product, amount in self.requirements.items()])}'''

    @property
    def produced_per_day(self):
        return self.amount_produced / self.production_time

    @property
    def required_per_day(self):
        return {product: amount / self.production_time for product, amount in self.requirements.items()}

    def _get_requirements(self, target: dict | None = None, amount: int = 1, red: int = 1) -> dict:
        if target is None:
            target = dict()
        req = amount * red
        if self not in target.keys():
            target[self] = 0
        target[self] += req
        new_red = req / self.amount_produced
        for product, amount in self.requirements.items():
            product._get_requirements(target=target, amount=amount, red=new_red)
        return target

# TODO create product subclasses that represent different types of production to make __str__ representation nicer
