import math

def add_two_numbers(n1,n2):
    sum = n1 + n2
    return sum
#--------------------------------------------------------------------
# 2.- Area of a circle is calculated as follows.
def circle_area(r):
    area = math.pi*r**2
    return area
#--------------------------------------------------------------------
# 3.- Write a function called add_all_nums.
def add_all_nums(nums):
    sum = 0
    if type(nums) == list:
        for num in nums:
            if type(num) == int:
                sum += num
            else:
                return f"One element in the list is not a number"
    else:
        if type(nums) == int:
                return
        else:
            return f"One element in the list is not a number"
    return sum
#--------------------------------------------------------------------
# 4.- Temperature in °C can be converted to °F.
def temperatureCF(cel):
    far = (cel * 9/5) + 32
    return far
#--------------------------------------------------------------------
# 5.- Write a function called check-season.
def check_season(month):
    if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
        return f"The current season is Autumn"

    elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
        return f"The current season is Winter"

    elif month == "MARCH" or month == "APRIL" or month == "MAY":
        return f"The current season is Spring"

    elif month == "JUNE" or month == "JULY" or month == "AUGUST":
        return f"The current season is Summer"
    else:
        return f"Invalid Data"
#--------------------------------------------------------------------
# 6.- Write a function called calculate_slope.
def calculate_slope(x1,x2,y1,y2):
    slope = (y2+y1)/(x2-x1)
    return slope
#--------------------------------------------------------------------
# 7.- Quadratic equation is calculated as follows.
def solve_quadratic_eqn(a,b,c):
    if b**2 - 4*a*c >= 0:
        sol1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        sol2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        return "The ecuation don't have any real solution"
    return sol1, sol2
#--------------------------------------------------------------------
# 8.- Declare a function named print_list.
def print_list(lis):
    if type(lis) == list:
        for i in lis:
            print(i)
    else:
        return f"{lis} is not a list"
#--------------------------------------------------------------------
# 9.- Declare a function named reverse_list.
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # Looping backward
        reversed_arr.append(arr[i])
    return reversed_arr
#--------------------------------------------------------------------
# 10.- Declare a function named capitalize_list_items.
capItems = []
def capitalize_list_items(li):
    if type(li) == list:
        for l in li:
            x = l.capitalize()
            capItems.append(x)
    else:
        return f"{li} is not a list"
    return capItems
#--------------------------------------------------------------------
# 11.- Declare a function named add_item
fruits = ["apple", "banana", "cherry"]
def add_item(li,item):
    li.append(item)
    return li
#--------------------------------------------------------------------
# 12.- Declare a function named remove_item.
def remove_item(li,item):
    if item in li:
        li.remove(item)
    else:
        return f"{item} is not in the list"
    return li
#--------------------------------------------------------------------
# 13.- Declare a function named sum_of_numbers.
def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
#--------------------------------------------------------------------
# 14.- Declare a function named sum_of_odds.
sumOdd = 0
def sum_of_odds(num):
    for i in range(num+1):
        if i % 2 != 0:
            sumOdd += i
    return sumOdd
#--------------------------------------------------------------------
# 15.- Declare a function named sum_of_even.
sumEven = 0
def sum_of_even(num):
    for i in range(num+1):
        if i % 2 == 0:
            sumEven += i
    return sumEven