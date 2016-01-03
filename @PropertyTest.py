class hi(object):
    """docstring for """
    def __init__(self, arg):
        self.arg = arg

    @property
    def food(self):
        print(self.arg)

s = hi("jello")

s.food
