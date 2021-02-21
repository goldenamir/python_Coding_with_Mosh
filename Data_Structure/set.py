# we use set for having unique elements in a list
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(first)

print(first | second)  # give us  the union of two sets
print(first & second)  # give us intersection of two sets

print(first-second)  # remove the intersection from the first list
print(first ^ second)  # adding elements which are only in one set

# set can not support INDEX, so we can use list instead of set
if 1 in first:
    print('yes')
