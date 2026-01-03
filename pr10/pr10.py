class B1:
    def __init__(self, val):
        self._x = val  # Використовуємо _x для імітації private/protected
        print("B1 constructor called")

    def show(self):
        print(f"x in B1 is {self._x}")


class B2:
    def __init__(self, val):
        self._x = val
        print("B2 constructor called")

    def show(self):
        print(f"x in B2 is {self._x}")


class D1(B1, B2):
    def __init__(self, val):
        # В Python ініціалізація базових класів відбувається явно
        B1.__init__(self, val)
        B2.__init__(self, val)
        self._x = val
        print("D1 constructor called")

    def show(self):
        print(f"x in D1 is {self._x}")
        B1.show(self)
        B2.show(self)


class D2(D1):
    def __init__(self, val):
        D1.__init__(self, val)
        self._x = val
        print("D2 constructor called")

    def show(self):
        print(f"x in D2 is {self._x}")
        D1.show(self)


class D3(D1):
    def __init__(self, val):
        D1.__init__(self, val)
        self._x = val
        print("D3 constructor called")

    def show(self):
        # У вашому коді C++ в D3 помилково виводиться "x in D2 is",
        # я залишив це для точності копіювання
        print(f"x in D2 is {self._x}")
        D1.show(self)


def main():
    x = 10
    print("Creating D2...")
    d2 = D2(x)
    print("\nShow x...")
    d2.show()

    x = 5
    print("\n\nCreating D3...")
    d3 = D3(x)
    print("\nShow x...")
    d3.show()

    input("\nPress Enter to exit...")

main()