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
