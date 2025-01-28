#A
costs = []
while True:
    cost = float(input("Enter the cost of an item (or -1 to stop): "))
    if cost == -1:
        break
    costs.append(cost)
#B
print("\n1. Display the cost list:")
print(costs)

print("\n2. Display the number of elements:")
print(len(costs))

print("\n3. The highest cost in the list:")
print(max(costs))

print("\n4. The lowest cost in the list:")
print(min(costs))

print("\n5. The total of the costs in the list:")
total = sum(costs)
print(total)

print("\n6. The average of the total costs:")
average = total / len(costs)
print(average)

print("\n7. Change the value of index 5 to a new value equal to 40:")
if len(costs) > 5:
    costs[5] = 40
    print("Updated list:", costs)
else:
    print("Index 5 does not exist in the list.")

print("\n8. Remove the fourth cost in your list:")
if len(costs) >= 4:
    print("List before deletion:", costs)
    del costs[3]
    print("List after deletion:", costs)
else:
    print("The list does not have a fourth element.")

print("\n9. Remove the first occurrence of 48 in the list:")
if 48 in costs:
    costs.remove(48)
    print("48 removed. Updated list:", costs)
else:
    print("48 was not found in the list.")
#C
costs_list = []
while True:
    cost = float(input("Enter the cost of an item (or -1 to stop): "))
    if cost == -1:
        break
    costs_list.append(cost)

#Convert the list to a tuple
costs_tuple = tuple(costs_list)

#Display the tuple
print("\nCosts stored in a tuple:")
print(costs_tuple)