from numba import njit
#import numpy as np
import time

start = time.time()


# def compute():
#     ans = sum(i for i in np.arange(2, 1000000) if i == fifth_power_digit_sum(i))
#     return str(ans)
# def fifth_power_digit_sum(n):
#     return sum(int(c)**5 for c in str(n))


@njit
def transform_to_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    digits = digits[::-1]
    return digits


@njit
def main(number):
    special_numbers = []
    while len(str(number)) < 7:
        sum_power = 0
        for x in transform_to_digits(number):
            x = x ** 5
            sum_power += x
        if sum_power == number:
            special_numbers.append(number)
        number += 1
    return special_numbers


if __name__ == "__main__":
    special_numbers = main(2)
    print(special_numbers)
    print(sum(special_numbers))
    # print(compute())
end = time.time()
print(end - start)
