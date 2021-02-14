numbers = [1, 2]
# print(numbers[3])  # cause an error
# in programming we prefer to have an exception, due to programers mistake
try:
    age = int(input('age: '))
except ValueError as ex:
    print('you did not enter a valid age.')
    print(ex)
    print(type(ex))
else:
    # if we do not have any exception, if we add integer.
    print('No exception were thrown')

print('execution continuing....')
