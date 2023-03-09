from time import time


def performance(func):
    '''
    Print the time it took to execute the function
    '''
    def wrap_func(*args, **kwargs):  # Define a function that will be executed before the function that is decorated
        t1 = time()  # Get the time before the function is executed
        result = func(*args, **kwargs)  # Execute the function
        t2 = time()  # Get the time after the function is executed
        print(f'{func.__name__} took {t2 - t1:.4f} s\n')  # Print the time it took to execute the function
        print(f'    Solution is ', result[0])  # Print the solution
        print(f'    Number of explored nodes is ', result[1])  # Print the number of explored nodes
        return result  # Return the result of the function
    return wrap_func  # Return the wrap_func function

