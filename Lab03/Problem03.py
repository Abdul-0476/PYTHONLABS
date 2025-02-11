A = [1, 2, 3, 4, 5]
B = [1, 2, 6, 7, 9]

itemsinA = list(set(A) - set(B))
itemsinB = list(set(B) - set(A))

# Creating dictionary with item appearances
item_dict = {item: ["A"] * (item in A) + ["B"] * (item in B) for item in set(A + B)}

print("Items in A not in B:", itemsinA)
print("Items in B not in A:", itemsinB)
print("Dictionary of item appearances:", item_dict)
