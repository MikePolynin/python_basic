def equation():
    print("Введите первую точку")
    x1 = float(input('X: '))
    y1 = float(input('Y: '))
    print("\nВведите вторую точку")
    x2 = float(input('X: '))
    y2 = float(input('Y: '))

    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff if x_diff != 0 else 0
    b = y2 - k * x2

    print("\nУравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b) if x_diff != 0 else print("y = ", b)


equation()
