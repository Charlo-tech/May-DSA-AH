efficiencies = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

# Arrange the numbers in ascending order
efficiencies.sort()

# Pair the first 38 numbers
pairs = [(efficiencies[i], efficiencies[i+1]) for i in range(0, 38, 2)]

# Find the sum of the differences between the pairs
minimum_cost = sum(abs(pair[0] - pair[1]) for pair in pairs)

print("The Minimum cost of given efficiencies is:", minimum_cost)
