from context.practise.func_time import TimeFunc, time_func


def sum_one_to_hundred():
    with time_func('adding'):
        sum = 0
        for i in range(1, 101):
            sum += i
    return sum


if __name__ == '__main__':
    sum_one_to_hundred()
