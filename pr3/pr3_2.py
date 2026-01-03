class CVstavka:
    def __init__(self):
        self.f = open("pr3.dat", "r+b")
        self.s = b""
        self.s1 = b""
        self.s2 = b""
        self.k = 0

    def __del__(self):
        self.f.close()

    def Procesing(self):
        self.f.seek(0)
        self.s1 = self.f.read()
        print(self.s1.decode(errors="ignore"))

        self.s = input("\nВведите фразу для сохранения в файл:\n").encode()
        self.k = int(input("Введите позицию вставки:\n"))

        self.s2 = self.s1[:self.k]
        tail = self.s1[self.k:]

        self.f.seek(0)
        self.f.write(self.s2)
        self.f.write(self.s)
        self.f.write(tail)
        self.f.truncate()

        self.f.seek(0)
        result = self.f.read()
        print("\n")
        print(result.decode(errors="ignore"))


obj = CVstavka()
obj.Procesing()
