def check_common(num):
    counter = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            counter += 1
    if counter == 1 and num > 1:
        return True
    else:
        return False


def truncatable_primes():
    num = 10
    common_list = []
    while len(common_list) < 11:
        if check_common(num):
            count = 0
            for i in range(1, len(str(num))):
                x = str(num)
                if check_common(int(x[i:])) and check_common(int(x[:-i])):
                    count += 1
                else:
                    break
            if count == len(x) - 1:
                yield num
                common_list.append(num)
        num += 1


print(sum(list(truncatable_primes())))
