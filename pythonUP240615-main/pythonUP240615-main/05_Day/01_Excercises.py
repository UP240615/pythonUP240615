b = list()
b = ["a","e","i","o","u"]
bmid = int(len(b)/2)

print(len(b))
print(b[0]," ",b[bmid]," ",b[-1])

mixed_data_types = ["Ann",18,1.70,False,"addres"]
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))

comMid = int(len(it_companies)/2)
print(it_companies[0]," ",it_companies[comMid]," ",it_companies[-1])

it_companies[6] = "Asus"
print(it_companies)

it_companies.append("Ubisoft")
print(it_companies)

it_companies.insert(4,"Sony")
print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)

result = '#;  '.join(it_companies)
print(result)

print(it_companies.index("IBM"))

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[3:6])

comMid = int(len(it_companies)/2)
comEnd = len(it_companies)
it_companies.pop(0)
print(it_companies)
it_companies.pop(comMid)
print(it_companies)
it_companies.pop(-1)
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = list()
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index("Redux") + 1,"Python")
full_stack.insert(full_stack.index("Redux") + 1,"SQL")
print(full_stack)



