import time

#Calculate the time spent in the function
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


#Log relevant info for debugging purposes

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished executing")
        return result
    return wrapper

#Slow the function

def slow(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(1)  # Simulate a slow operation
        return result
    return wrapper



#Convert the return value in some way

def convert_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result * 2
        return result
    return wrapper


#Validate some condition on the way in

def validate(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return func(*args, **kwargs)
        else:
            print("Invalid input")
    return wrapper