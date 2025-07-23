#list of tuples
data = [
    ('A', 1, 2),
    ('B', 3),
    ('C', 4, 5, 6),
    ('D',),
    ('E', 7, 8)
]
 
#sorting entire list
sorted_data = sorted(data)

# to extract first elements
result = list(zip(*sorted_data))[0]
 
print(list(result))

