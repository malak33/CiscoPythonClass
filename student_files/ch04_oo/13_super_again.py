class A:
    def __init__(self, foo):
        self.foo = foo


class B(A):
    def __init__(self, foo, bar):
        super().__init__(foo)
        self.bar = bar

b = B('foo_b', 'bar_b')


class C(B):
    def __init__(self):
        super(B, b).__init__('foo')


c = C()
print(b.foo)