import math
def evens_and_odds(num):
    numOdd = 0
    numEven = 0
    if num <= 0:
        return "The number isn't positive"
    else:
        for i in range(num+1):
            if i % 2 == 0:
                numEven += 1
            elif i % 2 != 0:
                numOdd += 1
        return numOdd,numEven
#--------------------------------------------------------------------
# 2.- Call your function factorial.
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
#--------------------------------------------------------------------
# 3.- Call your function is_empty.
def is_empty(var):
    return not bool(var)
#--------------------------------------------------------------------
# 4.- Write different functions which take lists.
def calculate_mean(num):
    return sum(num) / len(num) if num else None

def calculate_median(num):
    sorted_numbers = sorted(num)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def calculate_mode(num):
    frequency = {}
    max_freq = 0
    modes = []

    for n in num:
        frequency[n] = frequency.get(n, 0) + 1
        max_freq = max(max_freq, frequency[n])

    for n, freq in frequency.items():
        if freq == max_freq:
            modes.append(n)

    return modes if len(modes) > 1 else modes[0]

def calculate_range(num):
    return max(num) - min(num)

def calculate_variance(num):
    mean = calculate_mean(num)
    return sum((x - mean) ** 2 for x in num) / len(num)

def calculate_std(num):
    return math.sqrt(calculate_variance(num))