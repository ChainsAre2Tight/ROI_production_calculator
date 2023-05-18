from abc import ABC, abstractmethod


class FactoryInterface(ABC):
    name: str

    @abstractmethod
    def __str__(self):
        pass


class Factory(FactoryInterface):
    def __init__(
            self,
            name: str
    ):
        self.name = name

    def __str__(self):
        return self.name
