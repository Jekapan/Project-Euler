def main(n):
    different_number = []
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            different_number.append(a**b)
    return len(set(different_number))


if __name__ == "__main__":
    main(30)
