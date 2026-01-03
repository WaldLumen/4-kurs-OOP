from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self, x: float, y: float):
        self._center_x = x
        self._center_y = y
        self._angle = 0.0
        self._scale = 1.0
        self._visible = False

    @property
    def center(self):
        return (self._center_x, self._center_y)

    @property
    def angle(self):
        return self._angle

    @property
    def scale(self):
        return self._scale

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    def rotate(self, angle: float):
        self._angle += angle
        print(f"Фігуру повернуто на {angle}°")

    def move(self, dx: float, dy: float):
        self._center_x += dx
        self._center_y += dy
        print(f"Фігуру переміщено на вектор ({dx}, {dy})")


class Line(GeometricFigure):
    def __init__(self, x: float, y: float, length: float):
        super().__init__(x, y)
        self.__length = length

    def show(self):
        self._visible = True
        print(
            f"Пряма відображена. "
            f"Центр: {self.center}, "
            f"Довжина: {self.__length}, "
            f"Кут: {self._angle}°, "
            f"Масштаб: {self._scale}"
        )

    def hide(self):
        self._visible = False
        print("Пряма прихована.")

    def set_scale(self, scale: float):
        if scale > 0:
            self._scale = scale
            print(f"Масштаб змінено на {scale}")


line = Line(0, 0, 10)
line.show()
line.move(5, 3)
line.rotate(45)
line.set_scale(2)
line.hide()
