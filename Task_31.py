def main():
    list_of_combinations = []
    p1, p2, p5, p10, p20, p50, f1 = 1, 2, 5, 10, 20, 50, 100
    for a in range(3):
        for b in range(1 + int((200-100*a)/50)):
            for c in range(1+int((200-100*a-50*b)/20)):
                for d in range(1 + int((200-100*a-50*b-20*c)/10)):
                    for e in range(1 + int((200-100*a-50*b-20*c-10*d)/5)):
                        for f in range(1 + int((200-100*a-50*b-20*c-10*d-5*e)/2)):
                            for g in range(1 + (200-100*a-50*b-20*c-10*d-5*e-2*f)):
                                f2 = a * f1 + b * p50 + c * p20 + d * p10 + e * p5 + f * p2 + g * p1
                                if f2 == 200:
                                    list_of_combinations.append(f"({a} * f1) + ({b} * p50) + ({c} * p20) + "
                                                                f"({d} * p10) + ({e} * p5) + ({f} * p2) + ({g} * p1)")
    return list_of_combinations


if __name__ == "__main__":
    x = main()
    print(x[73678])
    print(len(x))


# def compute():
#     TOTAL = 200
#     ways = [1] + [0] * TOTAL
#     for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
#         for i in range(len(ways) - coin):
#           ways[i + coin] += ways[i]
#     return str(ways[-1])
#
#
# if __name__ == "__main__":
#     print(compute())
