import time
import threading


def calculate_square(numbers):
    result = []
    for number in numbers:
        time.sleep(0.2)
        result.append(number * number)
    return result


def calculate_cube(numbers):
    result = []
    for number in numbers:
        time.sleep(0.2)
        result.append(number * number * number)
    return result


numbers = [1, 2, 3, 4]
t = time.time()
t1 = threading.Thread(target=calculate_square, args=(numbers,))
t2 = threading.Thread(target=calculate_cube, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Time taken:", time.time() - t)
