class Foo:
    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)
    def non_copy_constructor(self):
        print("non copy constructor")
    def copy_constructor(self, orig):
        print("copy constructor")

a=Foo()  # this will call the non-copy constructor
b=Foo(a) # this will call the copy constructor