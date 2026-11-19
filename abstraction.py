"""
Abstraction: Hiding unnecessary details and showing only essential features
"""
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class Esewa(Payment):
    def pay(self):
        print("Process paymenet via esewa")