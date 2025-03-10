space = ' '
a = 'thirty'
b= 'days'
c='of'
d='Python'
print(a,space,b,space,c,space,d)

a = 'Coding'
b = 'for'
c = 'all'
print(a,space,b,space,c)

company = a+space+b+space+c
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
cut = company[0:6]
print(cut)
print(company.index('Coding'))
company2 = company.replace('Coding', 'Python')
print(company2)
company2 = company2.replace('all', 'Everyone')
print(company2)

sp = company.split(' ')
print(sp)

web = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(web.split(','))

com_index1 = company[0]
com_index2 = company[10]
print(com_index1,' - ', com_index2)

acronym = ''.join(word[0].upper() for word in company2.split())
print(acronym)
acronym = ''.join(word[0].upper() for word in company.split ())
print(acronym)

word1 = "Coding For All"

print(word1.index("C"))
print(word1.index("F"))

word2 = "Coding For All People"
print(word2.rindex("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.index("because")
end = sentence.rindex("because")
print(start, " ", end)
print(sentence[start:end+7])

#Does ''Coding For All' start with a substring Coding?
if (word1.index("Coding") == 0):
    print("YES")
else:
    print("NO")

#Does 'Coding For All' end with a substring coding?
if (word1.rindex("Coding") == len(word1)):
    print("YES")
else:
    print("NO")

word3 = "   Coding For All      "
print("|",word3.strip(" "),"|")

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())

#The following list contains the names of some of python 
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
#  Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lista = ""
for i in libraries:
    lista =lista + " " + i
print(lista)

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity")
print("Angie\t18\tMexico\tAguascalientes")