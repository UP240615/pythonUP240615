import random as rd
import string

def random_user_id():
    word = ''
    char = string.ascii_letters + string.digits
    for i in range(6):
        x = rd.randint(0,len(char))
        word += char[x]
    return word

def user_id_gen_by_user():
    word = ''
    numChar = int(input("Enter the number of characters: "))
    numUser = int(input("Enter the number of user names: "))
    char = string.ascii_letters + string.digits
    for c in range(numUser):
        for i in range(numChar):
            x = rd.randint(0,len(char))
            word += char[x]
        print(word)
        word = ''

def rgb_color_gen():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    rgb =  [r,g,b]
    return rgb

print(rgb_color_gen())