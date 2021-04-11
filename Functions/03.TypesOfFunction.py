def gree(name):
    print(f"hello {name}")


'''
we have to types of functions

1. preform a task (e.g., greet and print are functions which are preforming a task)
2. return a value (e.g., round(1.9) is a function which returns a value)

if put a print(preform a task fucntion) the result will be NONE
but, if put a print(return a value function), it will return a value to us


'''
# this is type of return value


def get_greet(name):
    return f"{name}"


message = get_greet('Amir')
file = open('content.txt', 'w')
file.open(message)
