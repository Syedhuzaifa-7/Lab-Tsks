def multiply_all(*args):
  if not args: 
    return 1 

  product = 1
  for num in args:
    product *= num
  return product

print(multiply_all(2, 3, 4))  # Output: 24