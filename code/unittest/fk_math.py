def one_equation(a,b):
    if a == 0:
        raise ValueError("参数错误")
    else:
        return b / a

def two_equation(a, b, c):
    if a == 0:
        raise ValueError("参数错误")
    elif b * b - 4 * a * c < 0:
        raise ValueError("无解")
    elif b * b - 4 * a * c == 0:
        return -b / (2 * a)
    else:
        r1 = (-b + (b * b - 4 * a * c) ** 0.5) / 2 / a
        r2 = (-b - (b * b - 4 * a * c) ** 0.5) / 2 / a
        return r1, r2
