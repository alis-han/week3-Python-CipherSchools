class A:
    def __init__(self):
        print("A init Created")

class B(A):
    def __init__(self):
        super().__init__()
        # super Helps to access base class methods
        print("B init Created")

abc=B()

# MRO---> Method Resolution Order
class A:
    pass
class B(A):
    x=5

class C(B):
    pass

# DFS
# If there is a loop solve branches differently

# Iteration Protocol
# __iter__
# __next__

a=range(5)

it=a.__iter__()
it.__next__()
