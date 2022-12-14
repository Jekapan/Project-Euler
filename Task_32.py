from math import floor


def has_pandigital_product(n):
    for i in range(1, floor(n**0.5)+1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n//i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


def compute():
    ans = list(i for i in range(1, 10000) if has_pandigital_product(i))
    return sum(ans)


if __name__ == "__main__":
    print(compute())
