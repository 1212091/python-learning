def binary_search(number_list, left, right, x):
    if right >= left:
        mid = left + (right - left) / 2
        if number_list[mid] == x:
            return mid
        elif number_list[mid] > x:
            return binary_search(number_list, left, mid - 1, x)
        else:
            return binary_search(number_list, mid + 1, right, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
a = 10

result = binary_search(arr, 0, len(arr) - 1, a)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
