import math
import numpy as np
import time
from numba import njit


@njit
def is_prime(n):
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        if (n % i) == 0:
            return False
    return True


@njit
def main():
    a = 0
    b = 0
    length = 0
    n1 = 0
    for x in np.arange(-999, 1000):
        for y in np.arange(-1000, 1001):
            prime_array = []
            n = 0
            while True:
                prime_number = n**2 + x*n + y
                if is_prime(prime_number):
                    prime_array.append(prime_number)
                    n += 1
                else:
                    break
            if length < len(prime_array):
                length = len(prime_array)
                a = x
                b = y
                n1 = n
    return a, b, n1


if __name__ == "__main__":

    start = time.time()
    a, b, n = main()
    end = time.time()
    print(f"произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное "
          f"количество простых чисел для последовательных значений n равна\n"
          f"{a} *{b} = {a*b}\n"
          f"длина последовательности -- {n}"
          f"\ntime -- {end - start}"
          )
