#A
table = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F']
]
#B
print("First two elements of each row:")
for row in table:
    print(row[:2])
#C
transposed_table = list(map(list, zip(*table)))
print("\nTransposed Table:")
for row in transposed_table:
    print(row)
#D
string_input = "HELLO"
result = list(string_input)
print("\nUsing list() constructor with a string:")
print(result)  # Outputs ['H', 'E', 'L', 'L', 'O']