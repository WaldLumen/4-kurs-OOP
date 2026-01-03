class CArray_2D:
    def __init__(self):
        self.array = []
        self.row = 0
        self.col = 0

    def Create_ar2D(self, rows, cols):
        self.row = rows
        self.col = cols
        self.array = [[0 for _ in range(cols)] for _ in range(rows)]

    def Clear(self):
        self.array.clear()
        self.row = 0
        self.col = 0

    def Input_ar2D(self):
        print("\nEnter numbers of array:")
        for i in range(self.row):
            for j in range(self.col):
                self.array[i][j] = int(
                    input(f"array[{i}][{j}] = ")
                )

    def Print_ar2D(self):
        print("\nNumbers of array:")
        for i in range(self.row):
            for j in range(self.col):
                print(f"array[{i}][{j}] = {self.array[i][j]}")

    def PrintNegative_ar2D(self):
        print("\nNegative numbers of array:")
        for i in range(self.row):
            for j in range(self.col):
                if self.array[i][j] < 0:
                    print(f"array[{i}][{j}] = {self.array[i][j]}")



rows = int(input("Enter the rows of array: "))
cols = int(input("Enter the columns of array: "))

obj1 = CArray_2D()
obj1.Create_ar2D(rows, cols)
obj1.Input_ar2D()
obj1.Print_ar2D()
obj1.PrintNegative_ar2D()

obj1.Clear()
