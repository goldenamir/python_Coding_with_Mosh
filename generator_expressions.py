from sys import getsizeof
values = [x*2 for x in range(10)]

# if instead of 10 on the above list, we have one billion, so the memory will be full
# In this case, we are using 'generator_expressions'
# unlike the lists, the generators do not save the values in memory
# touple are generators
values = (x*2 for x in range(10))
print(values)  # it will give us a generator

# we can not take 'len' of generators


values = (x*2 for x in range(100000))
print('gen: ', getsizeof(values))
values = [x*2 for x in range(100000)]
print('den: ', getsizeof(values))  # it takes more memory
