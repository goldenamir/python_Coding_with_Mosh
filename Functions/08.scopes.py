# where the variable is known is called 'scope' and

message = 'a'  # this is called global variable, this variable stay for longer time


def greet(name):
    message = 'a'  # the variable 'message' has a short life time and these are called 'LOCAL VAIRABLES'


'''
if we want to chagne the global varibale in the function
we are going to use it like below:
'''


def greet(name):
    global message
    message = 'b'  # now the global variable has been changed its value
    # but this is not good way, try to ignore it. THIS IS REALLY BAD PRACTICE.


def send_email(name):
    message = 'b'


# this will be return an error since the variable is known in the function
print(message)
