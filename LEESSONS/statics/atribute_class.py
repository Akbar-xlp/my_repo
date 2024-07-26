class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    @staticmethod
    def info(a, b):
        print("This is a static method")
        print(a + b)


Shape.info(5, 5)
ob_1 = Shape(1, 2)
ob_1.info(5, 5)
print(ob_1.area())


class Counter:
    count = 0

    def __init__(self, name):
        self.name = name
        Counter.count += 1

    @staticmethod
    def get_count_objects():
        print(f"All objects = {Counter.count}")


obj_1 = Counter("ob_1")
obj_2 = Counter("ob_2")
Counter.get_count_objects()
obj_3 = Counter("obj_3")
Counter.get_count_objects()
