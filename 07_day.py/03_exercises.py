age_list = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age_list)     

if len(age_set) == len(age_list):
    print('The set and the list are equal')
elif len(age_set) > len(age_list):
    print('set is bigger')
else:
    print('List is bigger')

'''
String: Text-based data.
List: Ordered, mutable collection of items.
Tuple: Ordered, immutable collection of items.
Set: Unordered collection of unique items.
'''


sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split())
print(f'The number of unique words is {len(words)}')