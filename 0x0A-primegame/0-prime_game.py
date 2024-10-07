#!/usr/bin/python3
"""Find prime"""


def isPrime(x):
    """detec if num is prime"""
    if x == 1:
        return False
    # range ends with sqrt(x), after this num all digits are doubled
    for m in range(2, int(x**0.5) + 1):
        if x % m == 0:
            return False
    return True


def isMulti(num, num_range):
    """ return multi of a digit"""
    return [i for i in num_range if i % num == 0]
    # multi = []
    # for i in (num_range):
    #     if i % num == 0:
    #         multi.append(i)
    # # print("multi list", multi)
    # return multi


def isWinner(x, nums):
    """finds a prime
    x: count of rounds
    nums: list of nums
    return the winner
    """
    ben = 0
    mari = 0

    # handle edge cases
    if len(nums) == 0 or x <= 0:
        return None

    # loop through the list
    for num in nums:
        # every num represent a new round st mare and ends with bin
        # handle if its 1
        if num == 1 or num == 0:
            # nothing fo mari to pick
            ben += 1
            continue

        num_range = [i for i in range(1, num + 1)]
        # print("unum range in big loop",num_range, len(num_range))
        role = 0
        while len(num_range) != 1:
            # check for prime
            # print("num range in small lop", num_range)
            for digit in num_range:
                if isPrime(digit):
                    remove_list = isMulti(digit, num_range)
                    for m in remove_list:
                        num_range.remove(m)
                    role += 1
                    break
        # score at the end of th turn
        if role % 2 != 0:
            mari += 1
        else:
            ben += 1

        # print("num_range", num_range)

    if ben > mari:
        return "Ben"
    elif ben < mari:
        return "Maria"
    else:
        return None
