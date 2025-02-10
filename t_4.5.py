# На відрізку [0, 2] знайдіть корінь рівняння
# 𝑥³ + 4𝑥² + 𝑥 − 6 = 0.

def f(x):
    return x ** 3 + 4 * (x ** 2) + x - 6

def solve(a, b):
    eps = 1e-7
    l, r = a, b
    while r - l > eps:
        m = (l + r) / 2.0
        if f(m) > 0:
            r = m
        else:
            l = m
    return l

if __name__ == '__main__':
    print(f"Root = {solve(0, 2):.6f}")