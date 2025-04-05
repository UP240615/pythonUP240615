for i in range (-1,11,1):
    print(f"For loop: {i}")

x = 0
while x != 11:
    print(f"While loop: {x}")
    x = x+1
#--------------------------------------------------------------------
# 2.- Iterate 10 to 0 using for loop, do the same using while loop.
for i in range (10,0,-1):
    print(f"For loop: {i}")

x = 10
while x != -1:
    print(f"While loop: {x}")
    x = x-1
#--------------------------------------------------------------------
# 3.- Write a loop that makes seven calls to print().
for i in range (0,8,1):
    print(f"#"*i)
#--------------------------------------------------------------------
# 4.- Use nested loops to create the following.
for i in range(8):
    for x in range(8):
        print(f"#", end=f" ")
    print()
#--------------------------------------------------------------------
# 5.- Print the following pattern.
for i in range(11):
    print(f"{i} x {i} = {i**2}")
#--------------------------------------------------------------------
# 6.- Iterate through the list.
libraries = ['Python', 'Numpy','Pandas','Django', 'Flask']

i = 0
for lib in libraries:
    print(f"Element {i}: {lib}")
    i = i + 1
#--------------------------------------------------------------------
# 7.- Use for loop to iterate from 0 to 100 and print only even numbers.
for i in range(0,101,1):
    if i % 2 == 0:
        print(i)
#--------------------------------------------------------------------
# 8.- Use for loop to iterate from 0 to 100 and print only odd numbers.
for i in range(0,101,1):
    if i % 2 != 0:
        print(i)