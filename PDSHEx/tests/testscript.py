def cube_fromscript(x):
    """Cube a number, x"""
    return x**3


for i in range(10, 15):
    print(f"{i} cube is {cube_fromscript(i)}")
