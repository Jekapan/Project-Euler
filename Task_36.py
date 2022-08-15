import numpy as np
import time

start = time.monotonic()

polindroms_sum = [i for i in np.arange(1, 1000000) if str(i) == str(i)[::-1] if str(bin(i)[2:]) == str(bin(i)[2:])[::-1]]

# polindroms_sum = 0
#
# for i in np.arange(1, 1000000):
#     if str(i) == str(i)[::-1]:
#         if str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
#             polindroms_sum += i


print(f"{sum(polindroms_sum)}\ntime of calculation = {time.monotonic() - start}")
