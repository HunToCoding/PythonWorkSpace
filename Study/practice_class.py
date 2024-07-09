class Unit :
    def __init__(self):
        print("Unit")

class Flyable:
    def __init__(self):
        print("Flyable")

class FlyUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# super는 마지막 상속만 적용됨
dropship = FlyUnit()
