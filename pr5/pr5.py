class Vstring:
    many = 0

    def __init__(self, text):
        self.s = text
        self.length = len(text)
        Vstring.many += 1

    def __del__(self):
        Vstring.many -= 1

    @staticmethod
    def Number():
        return Vstring.many

    def get(self):
        print(self.s)


print("Количество объектов Vstring:", Vstring.Number())

u = Vstring("12345")
print("Количество объектов Vstring:", Vstring.Number())

v = Vstring("12345")
print("Количество объектов Vstring:", Vstring.Number())

print("Значение объекта v:", end=" ")
v.get()
print()

for i in range(3):
    print("Количество объектов Vstring:", Vstring.Number())
    v = Vstring("12345")
    print("Количество объектов Vstring:", Vstring.Number())
    del v
