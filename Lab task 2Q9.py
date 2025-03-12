def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def my_function():
    print("Inside my_function")

my_function()