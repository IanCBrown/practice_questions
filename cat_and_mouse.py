# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    x_diff = abs(z - x)
    y_diff = abs(z - y)

    if x_diff == y_diff:
        return "Mouse C"
    elif x_diff < y_diff:
        return "Cat A"
    else:
        return "Cat B"
