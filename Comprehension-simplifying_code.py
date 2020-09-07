# List Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
my_list1 = []
for n in nums:
    my_list.append(n)

    # I want 'n*n' for each 'n' in nums
    my_list1.append(n * n)
print(my_list)
# simplified

print([n for n in nums])

print(my_list1)
# simplified
print([n*n for n in nums])

# Using a map + lambda
my_list2 = map(lambda n: n*n, nums)
print(list(my_list2))

# I want n for each n in nums if n%2 == 0
my_list3 = [n for n in nums if n % 2 == 0]
print(my_list3)

#Using a filter + lambda
my_list3_lamda = filter(lambda n: n%2 == 0, nums)
print(list(my_list3_lamda))


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
mylist_4 = []
for letter in 'abcd':
    for num in range(4):
        mylist_4.append((letter, num))
print(mylist_4)

# same with list comprehensions
my_list_comp4 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list_comp4)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict_comp = {name: hero for name, hero in zip(names, heros)}
print(my_dict_comp)

# If name not equal to Peter
my_dict_comp = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict_comp)

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set

my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_gen = (n*n for n in nums)

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

for i in my_gen:
    print(i)
