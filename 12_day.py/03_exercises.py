import random as rd
import string as st
fruits = ["manzana", "plátano", "naranja", "uva", "sandía", 
          "pera", "kiwi", "mango", "fresa", "cereza"]

def shuffle_list(lt):
    rd.shuffle(lt)
    return lt

def unique_nums():
    nums = set()
    while len(nums) <= 7:
        x = rd.randint(0,len(st.digits)-1)
        nums.add(st.digits[x])
    return nums

print(unique_nums())