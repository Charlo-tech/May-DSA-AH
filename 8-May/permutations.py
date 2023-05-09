# This is python code to iterate through possibble permutations of 1867 and find those divisible by 7 without a remainder.
from itertools import permutations

num_str = '1867'
digits = list(map(int, num_str))

divisible_permutations = []
for p in permutations(digits):
    num = int(''.join(map(str, p)))
    if num % 7 == 0:
        divisible_permutations.append(num)

if divisible_permutations:
    smallest = min(divisible_permutations)
    largest = max(divisible_permutations)
    avg = (smallest + largest) / 2
    print("The smallest permutation is:", smallest)
    print("The largest permutation is:", largest)
    print("The average is:", avg)
else:
    print("No permutation is divisible by 7.")
