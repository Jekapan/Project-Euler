def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def special_factorial(n):
    compare = 0
    for j in str(n):
        compare += factorial(int(j))
    if compare == n:
        return True
    return False


def compute():
    ans = list(i for i in range(3, 100000) if special_factorial(i))
    return sum(ans), ans


if __name__ == "__main__":
    print(compute())
