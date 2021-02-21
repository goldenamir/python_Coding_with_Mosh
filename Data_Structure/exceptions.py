numbers = [1, 2]
# print(numbers[3])  # cause an error
# in programming we prefer to have an exception, due to programers mistake
try:
    age = int(input('age: '))
    xfactor = 10/age
# except ValueError as ex:
#     print('you did not enter a valid age.')
#     print(ex)
#     print(type(ex))
# except ZeroDivisionError:
#     print('age can not be zero')

# having several exception
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age.')
else:
    # if we do not have any exception, if we add integer.
    print('No exception were thrown')

print('execution continuing....')


''' Cleaning up '''
try:
    file = open('app.py')
    age = int(input('age: '))
    xfactor = 10/age

except (ValueError, ZeroDivisionError):
    print('you did not enter a valid age.')

else:
    print('No exceptions were thrown.')

finally:
    file.close()  # to release memory

''' with statement ''''
try:
    with open('app.py') as file:  # in this way we do not need to close the opened file
        print('file is opened.')

    age = int(input('Age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print('you did not enter a valid age.')
else:
    print('no exception were thrown.')


''' Raising exceptions ''''


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less. ')
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


''' Cost of raising exceptions 

It is better to do not use exception in codes which are costly. Instead we can use if statement. '''
