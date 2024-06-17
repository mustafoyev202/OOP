import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} milliseconds")
        return result

    return wrapper


@time_it
def calculate_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


@time_it
def calculate_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


if __name__ == "__main__":
    numbers = range(1, 1000)
    square = calculate_square(numbers)
    cube = calculate_cube(numbers)
