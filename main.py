class Animals:
    def __init__(self):
        self.can_run = False
        self.can_fly = False

class Horse(Animals):
    def __init__(self):
        super().__init__()
        self.can_run = True

class Eangle(Animals):
    def __init__(self):
        super().__init__()
        self.can_fly = True

class Pegaus(Horse, Eangle):
    pass

p = Pegaus()
print(p.can_run)
print(p.can_fly)
