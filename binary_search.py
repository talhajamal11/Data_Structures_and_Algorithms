# Practicing a Binary Search Algorithm
# Creating a Binary Search Algorithm that takes in a list and value to search for within the list
import math


def binary_search(arr, value):
    lower_bound = 0
    upper_bound = len(arr) - 1
    steps = 0
    print(lower_bound, upper_bound)

    while lower_bound <= upper_bound:
        mid = math.floor(int((upper_bound + lower_bound) / 2))
        print(mid)
        if value == arr[mid]:
            steps += 1
            return mid, steps
        elif value < arr[mid]:
            upper_bound = mid - 1
            steps += 1
            print(upper_bound)
        elif value > arr[mid]:
            lower_bound = mid + 1
            steps += 1
            print(lower_bound)
    return "Value not found in Array"


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    print(binary_search(array, 6))
