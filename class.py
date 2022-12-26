# class
class drawPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Drawing....")

    def move(self):
        print("Moveing...")

    def calc(self):
        print(f'Sum ===> {self.x + self.y}')


point1 = drawPoint(10, 20)
point1.calc()
# print(point1.x)
