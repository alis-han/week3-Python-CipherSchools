object
a=5
isinstance(a,object)
type(int)

class A:
    name="Jatin"
    marks=50
    # BluePrints
type(A)

def func():
    print("HEllo")
type(func)
isinstance(func,object)
# Function objects are callable

class B:
    def __call__(self):
        print("You called me")

func.__call__()
b=B()

class Exponent:
    globals=""
    def __init__(self,n):
        self.n=n
    def __getitem__(self,x):
        return x**self.n

e=Exponent()


