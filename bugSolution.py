def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [10, 0, 30, 40, 50]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero is: {average_with_zero}")

#Robust solution handling potential exceptions
def calculate_average_robust(numbers):
    try:
        if not numbers:
            return 0
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(f"Error: {e}")
        return None # Or handle appropriately

my_list_with_string = [10, "hello", 30] # Example of invalid input
result = calculate_average_robust(my_list_with_string)