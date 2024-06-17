import time
import multiprocessing

square_result = []


def calculate_square(numbers):
    global square_result
    for number in numbers:
        square_result.append(number * number)
        print(number * number)
    print("Square result:", square_result)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    p1.start()
    p1.join()
    print("Result" + str(square_result))
