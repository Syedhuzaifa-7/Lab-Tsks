def operate(func, num1, num2):
  return func(num1, num2)

def add(x, y):
  return x + y

result1 = operate(add, 5, 3)
print(result1)