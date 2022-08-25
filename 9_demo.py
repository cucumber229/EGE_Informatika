import collections


def counter_of_doubles(arr):
    """проверяет что в строке только одно число повторяется дважды"""
    count = 0
    for i in arr:
        if i[1] == 2:
            count += 1
    if count == 1:
        return True
    if count == 0:
        return False


def sum_of_doubles_and_sr_of_nodoubles(arr):
    '''проверяет что среднее арифметическое неповторяющихся чисел строки не больше
суммы повторяющихся чисел'''
    if not counter_of_doubles(arr):
        return True
    else:
        repeat = 0
        non_repeat = []
        for i in arr:
            if i[1] == 2:
                repeat += (i[0] * 2)
            else:
                non_repeat.append(i[0])
        print(arr, sum(non_repeat) / len(non_repeat), repeat, sum(non_repeat) / len(non_repeat) <= repeat)
        return sum(non_repeat) / len(non_repeat) <= repeat


def main():
    a = open('test').read().splitlines()
    count = 0
    for x in a:
        s = x.split('\t')
        s = list(map(int, s))
        s = collections.Counter(s).most_common()
        if counter_of_doubles(s) and sum_of_doubles_and_sr_of_nodoubles(s):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
