from abc import ABC, abstractmethod
from backend.factory import FactoryInterface


class ProductInterface(ABC):
    product_type: str
    production_time: float | int
    requirements: dict | None
    amount_produced: int
    production_facility: FactoryInterface

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_requirements(
            self,
            target: dict | None = None,
            amount: int = 1,
            red: int = 1,
            include: bool = True
    ) -> dict:
        pass


class Product(ProductInterface):
    # TODO create product subclasses that represent different types of production to make __str__ representation nicer

    def __init__(
            self,
            product_type: str,
            production_time: float | int,
            amount_produced: int,
            production_facility: FactoryInterface,
            requirements: dict | None,
    ):
        self.product_type = product_type
        self.production_time = production_time
        self.amount_produced = amount_produced
        self.requirements = requirements
        self.production_facility = production_facility

    def __str__(self):
        return f'''Product "{self.product_type}" x{self.amount_produced} takes {
        self.production_time} days to produce at {self.production_facility} and requires {
        ', '.join([f'{product.product_type} x {amount}' for product, amount in self.requirements.items()])}'''

    def get_requirements(
            self,
            target: dict | None = None,
            amount: int = 1,
            red: int = 1,
            include: bool = True
    ) -> dict:
        if target is None:
            target = dict()
        req = amount * red
        if include:
            if self not in target.keys():
                target[self] = 0
            target[self] += req
        new_red = req / self.amount_produced
        for product, amount in self.requirements.items():
            product.get_requirements(target=target, amount=amount, red=new_red, include=True)
        return target
