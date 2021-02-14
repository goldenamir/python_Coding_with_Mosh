# for better printing
from pprint import pprint


sentence = 'This is a common interview question'

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequnecy_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print('high frequnt charecters: ', char_frequnecy_sorted[0])

pprint(char_frequency, width=1)
