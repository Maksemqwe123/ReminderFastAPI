import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result_time = func(*args)
        end_time = time.time()
        print(f'Time complete def: {end_time - start_time:.10f}')
        return result_time

    return wrapper


@timer
def search(lst_, low_, high_, x_):
    count = 0
    for i in range(low_, high_):
        count += 1
        if lst_[i] == x_:
            return i, count

    else:
        return -1


# lst = [i for i in range(1, 10000)]
# x = 85
# result = search(lst, 0, len(lst) - 1, x)
# if result != -1:
#     print(f'Number {x} find in list on index {result[0]}. Number count {result[1]}')
# else:
#     print('Number not found')


@timer
def binary_search(lst_, low_, high_, x_):
    count = 0
    while low_ <= high_:
        count += 1
        mid = (low_ + high_) // 2
        if lst_[mid] == x:
            return mid, count

        elif lst_[mid] > x:
            high_ = mid - 1

        else:
            low_ = mid + 1

    else:
        return -1


lst = [i for i in range(1, 100000)]
x = 10000
result = binary_search(lst, 0, len(lst) - 1, x)
if result != -1:
    print(f'Number {x} find in list on index {result[0]}. Number count {result[1]}')
else:
    print('Number not found')
