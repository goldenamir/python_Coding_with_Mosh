'''
the first paramter is called 'required paramet', 
there is no way to put required argument after 'default paramer'
'''


def increment(number, by=1):  # sicne we have given a value to the function there is no need to fill it but we can change it
    return number + by


print(increment(9))
print(increment(9, 2))
