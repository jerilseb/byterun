class Foo:
    x = 1
    def __init__(self, y):
        self.y = y

    def add(self, z):
        print "Hello there"
        return self.x + self.y + z


foo = Foo(33)
val = foo.add(3)
print val
