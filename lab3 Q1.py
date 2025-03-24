my_list = [10, "hello", 3.14, True, [1, 2, 3], {"name": "Alice"}]

for item in my_list:
  print(item)

# Accessing elements using indexing
print("Element at index 0:", my_list[0])
print("Element at index 1:", my_list[1])
print("Element at index 4:", my_list[4])
print("Element at index 5:", my_list[5]) 
print("Element at index -1:", my_list[-1]) 

# Slicing the list
print("Slice from index 1 to 4:", my_list[1:4])
print("Slice from beginning to index 3:", my_list[:3])
print("Slice from index 3 to the end:", my_list[3:])
print("Slice every other element:", my_list[::2])
print("Reverse the list:", my_list[::-1])

# Modifying list elements
my_list[0] = 20 
print("Modified first element:", my_list[0])

my_list[1] = "world" 
print("Modified second element:", my_list[1])

print("Modified List:", my_list)