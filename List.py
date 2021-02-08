""" Accessing Items """

letters = ["a", "b", "c", "d"]
letters[0] = 'A'
print(letters[0])
print(letters[-1])
print(letters[0:3])
print(letters[:3])
print(letters[:])  # it takes whole elements
print(letters[::2])  # takes each two element

numbers = list(range(20))
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])  # it counts from end to start

""" List Unpacking """"

numbers = [1, 2, 3], 9
first, second, third = numbers
first, second, *other = numbers  # just the two element will be saved
# it will save the first and last element and save other elements in others
first, *other, last = numbers


def multiply(*numbers):
    return numners*numbers


print(multiply(1, 2, 3, 4, 5))

first = numbers[0]
second = numbers[1]
third = numbers[2]

""" Looping over Lists """"
letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):  # for getting index
    print(letter)
    print(index, letter)
    # print(letter[0], letter[1]) # first one gives us index and the second the value

""" Adding or removing items """"
letters = ['a', 'b', 'c']
letters.append('d')  # adding
print(letters)
# adding element in specific position
letters.insert(0, "-")  # adding in first place

# remove
letters.pop(0)  # removing from first index
letters.pop()  # remove from last of the list
letters.remove('b')  # loop in list and remove all 'b'from the list
del letters[1:3]  # we can remove range of items

""" finding item """"

letters = ['a', 'b', 'c']
print(letters.index('a'))  # gives us the index of 'a'
print(letters.index('d'))  # there is no 'd'so we will face an error

if 'd' in letters:
    print(letters.index('d'))  # with this code we will not have any error

# there is better way to handle the index of not existing element
print(letters.count('d'))  # now we wonot have any error

""" Sorting lists """"
numbers = [3, 51, 2, 8, 6]
numbers.sort()  # sort in ascending order
print(numbers)
numbers.sort(reverse=Ture)  # sort in descending order
sorted(numbers)  # give new sorted list and the original one has not been sorted
print(sorted(numbers))


items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 30)
]
# for sorting the toppel


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

""" Lambdas function """"

items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 30)
]
# for sorting the toppel
# def sort_item(item): # has been written as lambda function
#     return item[1]

items.sort(key=lambda item: item[1])  # lambda is unanymous function
print(items)

""" Map function """
items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 30)
]

# we wanna to make a list of numbers
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# better way is MAP function
prices = list(map(lambda item: item[1], items))
print(prices)

""" Filter function """"
filtered = []

prices_bigger_than_ten_dollar = list(filter(lambda item: item[1] >= 10, items))

""" List comprehenstions """
# [expression for item in items]
prices = [item[1] for item in items]  # it is more better than other methods

# filtered = [expression for item in items]
filtered = [if item[1] >= 10 for item in items]


""" zip function """"
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))
print(list(zip('abc', list1, list2)))


""" stacks """
# LIFO last in first out
# this topic is related to data structure but we can use it in python programming as well.
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print(browsing_sessin[-1])
if not browsing_session:  # this checks we have an empty session/list
    print('disable')

""" Queues """"
# LIFO : Last in First out
