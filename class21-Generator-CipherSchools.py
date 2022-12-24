# GENERATORS
# yield KEYWORD
# generator is a iterator
def generate_squares(n):
    for i in range(n):
        yield i**2

for i in generate_squares(100):
    print(i)

a=generate_squares
type(a)