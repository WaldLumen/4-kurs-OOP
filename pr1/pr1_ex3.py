class CArray_1D:
    def __init__(self):
        self.array = []
        self.size = 0

    def Create_ar1D(self, n):
        self.size = n
        self.array = [0] * n

    def Clear(self):
        self.array.clear()
        self.size = 0

    def Input_ar1D(self):
        print("\nEnter numbers of array:")
        for i in range(self.size):
            self.array[i] = int(input(f"array[{i}] = "))

    def Print_ar1D(self):
        print("\nNumbers of array:")
        for i in range(self.size):
            print(f"array[{i}] = {self.array[i]}")

    def NumKr7_ar1D(self):
        count = 0
        for i in range(self.size):
            if self.array[i] % 7 == 0:
                count += 1
        return count

    def SumKr7_ar1D(self):
        total = 0
        for i in range(self.size):
            if self.array[i] % 7 == 0:
                total += self.array[i]
        return total

    def PrintKr7_ar1D(self):
        print("\nNumbers of array / 7:")
        for i in range(self.size):
            if self.array[i] % 7 == 0:
                print(f"array[{i}] = {self.array[i]}")


size = int(input("Enter the size of array: "))

obj1 = CArray_1D()
obj1.Create_ar1D(size)
obj1.Input_ar1D()
obj1.Print_ar1D()

num = obj1.NumKr7_ar1D()
summ = obj1.SumKr7_ar1D()

print(f"\nNumber = {num}")
print(f"\nSum = {summ}")

obj1.PrintKr7_ar1D()
obj1.Clear()
