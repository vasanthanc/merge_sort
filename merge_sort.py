INITIAL = 0
def sorting(arr):
    arr_length = len(arr)
    if arr_length > 1:
        mid = arr_length//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        deep_left = sorting(left_half)
        deep_right = sorting(right_half)

        left_counter = right_counter = arr_counter = INITIAL

        while left_counter < len(deep_left) and right_counter < len(deep_right):
            if deep_left[left_counter] > deep_right[right_counter]:
                arr[arr_counter] = deep_right[right_counter]
                right_counter += 1
            else:
                arr[arr_counter] = deep_left[left_counter]
                left_counter += 1
            arr_counter += 1

        while left_counter < len(deep_left):
            arr[arr_counter] = deep_left[left_counter]
            left_counter += 1
            arr_counter += 1

        while right_counter < len(deep_right):
            arr[arr_counter] = deep_right[right_counter]
            right_counter += 1
            arr_counter += 1

    return arr
if __name__ == '__main__' :
    arr = [12,8,5,7,2,8,9,1,2,10]
    res = sorting(arr)
    print(res)
