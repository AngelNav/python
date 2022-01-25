from functools import reduce

# filter
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

odd = list(filter(lambda x: x % 2 != 0, my_list))

print(odd)

# map
map_list = [1, 2, 3, 4, 5]

square = list(map(lambda x: x**2, map_list))

print(square)

# reduce
reduce_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a *b, reduce_list)

print(all_multiplied)