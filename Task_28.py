def main():
    n = 1
    d1 = 1
    d2 = 1
    x = 1
    sum = 1
    while n<1001:
        d1 = d1 + 2 * n
        d2 = d2 + 4*x
        if n % 2 == 0:
            x +=1
        n += 1
        sum = sum + d1 + d2
    return sum




if __name__ == "__main__":
    n = main()
    print(f"sum of diagonals = {n}")