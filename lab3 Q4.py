fruits = ["apple", "banana", "cherry"]

# For loop iteration:
print("For loop:")
for fruit in fruits:
    print(fruit)

# While loop iteration:
print("\nWhile loop:")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Using enumerate for index tracking:
print("\nEnumerate loop:")
for index, fruit in enumerate(fruits):
    print(index, fruit)