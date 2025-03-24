numbers = [1, 2, 3] 
numbers.append(4) 
numbers.extend([5, 6]) 
print(numbers)   
 
numbers.insert(2, 99) 
print(numbers) 
numbers.remove(99)  
print(numbers) 
last_item = numbers.pop()
print(last_item) 

numbers.sort() 
numbers.reverse()
print(numbers)