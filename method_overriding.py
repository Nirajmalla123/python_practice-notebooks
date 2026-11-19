"""
Method overriding: a child provides its own implementation of the method
 that already exists in parent class
--same method name
--same parameter
--Happens only in inheritance

"""

class Animal:
    def sound(self):
        print("Animal produce sound")

class Dog(Animal): #overridden method
    def sound(self):
        print("Dog barks")

d=Dog()
d.sound()

class Bank:
    def interest(self):
        print("General interest rate:2.7%")

class HimalaynBank(Bank):
    def interest(self):
        print("Himalayan Bank interest rate: 3%")

class GlobalIME(Bank):
    def interest(self):
        print("GlobalIME nank interest rate:3.2%")

class Siddartha(Bank):
    pass

hmb=HimalaynBank()
hmb.interest()

sid=Siddartha()
sid.interest()


