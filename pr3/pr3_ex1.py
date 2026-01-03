class CSlov:
    def __init__(self):
        self.f = open("pr3.txt", "r", encoding="utf-8")
        self.k = 0
        self.c = ''
        self.c1 = 'z'

    def __del__(self):
        self.f.close()

    def Procesing(self):
        while True:
            self.c = self.f.read(1)
            if not self.c:
                break
            if self.c == ' ':
                if self.c != self.c1:
                    self.k += 1
            self.c1 = self.c
        print("Words amount: ", self.k + 1)


obj = CSlov()
obj.Procesing()
