numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)  # print individual numebrs
# in the list we can unpack by below code
print(*numbers)


values = list(range(5))
values = [*range(5), *'hello']
print(values)

# unpacking two lists and concatenate them together
first = [1, 2]
secomnd = [3]
values = [*first, 'a', *second, *'hello']
print(values)


# how make a unpacking on the dictionary, shown as below
first = {'x': 1}
second = {'x': 10, 'y': 2}
combined = {**first, **second, 'z': 3}
print(combined)
