# Practicing a Binary Search Algorithm
# Creating a Binary Search Algorithm that takes in a list and value to search for within the list

def binary_search(arr, value):
    lower_bound = 0
    upper_bound = len(arr)

    mid = int((upper_bound) / 2)

    count = 1

    while arr[mid] != value:
        if arr[mid] > value:
            mid = int((lower_bound + mid) / 2)
            count += 1
        elif arr[mid] < value:
            mid = int((upper_bound + mid) / 2)
            count += 1
    return arr[mid], count


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(array, 2))
