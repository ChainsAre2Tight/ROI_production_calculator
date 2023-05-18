from abc import ABC, abstractmethod


class FactoryInterface(ABC):
    name: str


class Factory(FactoryInterface):
    def __init__(
            self,
            name: str
    ):
        self.name = name
