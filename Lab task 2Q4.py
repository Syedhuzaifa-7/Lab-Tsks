global_variable = 10  

def modify_global():
  global global_variable 
  global_variable = 20 

print(f"Global variable before modification: {global_variable}")
modify_global()

print(f"Global variable after modification: {global_variable}")