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
