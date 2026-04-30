#studying super() = fuction used in a child class to call methos from a parent class(superclass)
# allows you to extend the funcitionality of the inherited methods
# https://www.youtube.com/watch?v=IbMDCwVm63M&t=2768s

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, height):
        super().__init__(color, is_filled)
        self.height = height



circle = Circle(color="red", is_filled=True, radius=5)



print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

