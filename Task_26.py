def count_repeat(number):
    list_1 = [10]
    while ((list_1[-1]) % number)*10 not in list_1:
        list_1.append((list_1[-1] % number)*10)

    return len(list_1)-list_1.index((list_1[-1] % number)*10)


repeat_lenth = 0
relevent_i = 2

for i in range(2, 1000):
    if count_repeat(i) >= repeat_lenth:
        repeat_lenth = count_repeat(i)
        relevent_i = i
        print(f"{i}-{repeat_lenth}")
print(relevent_i)