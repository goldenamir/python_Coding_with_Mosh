''' 
If we want to have more than arguments which is defined in the function definition
we will use xargs
'''


def multi(*numbers):
    total = 1
    for number in numbers:
        total += number

    return total


print(multi(2, 3, 4, 5))
