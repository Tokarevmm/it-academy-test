def unique_sorted(arr):
    unique_dict = {}

    for element in arr:

        if element not in unique_dict:
            unique_dict[element] = True

    return sorted(unique_dict.keys())

arr = [3, 2, 1, 2, 3, 4, 5, 4, 6]
print(unique_sorted(arr))