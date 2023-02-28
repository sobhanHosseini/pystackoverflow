class Test:
    def __init__(self, a):
        self.a = a
    
    @classmethod
    def g(cls):
        print(cls.a)

af = Test(1234)

af.g()
    