"""
Encapsulation:Wrapping data and methods together and hiding from outside access
achieved via:
public:default
protected:default
private:_variable
"""

# class Bank:
#     def __init__(self):
#         self.__balance = 10000  # private attribute

#     def show(self):
#         print(f"Balance: {self.__balance}")


# class HBL(Bank):
#     def display(self):
#         print(self.__balance)  # not allowed


# b = Bank()
# b.show()

# hbl = HBL()
# hbl.display()


class Demo:
    def __init__(self):
        self.name = "Ram"  # public attribute
        self._age = 20  # protected attribute
        self.__salary = 5000  # private attribute

    def show_name(self):  # public method
        print(self.name)

    def _show_age(self):  # protected method
        print(self._age)

    def __show_salary(self):  # private method
        print(self.__salary)

    def show(self):
        self.__show_salary()

d = Demo()
print(d.name)
print(d._age)

d.show_name()
d._show_age()
d.show()


