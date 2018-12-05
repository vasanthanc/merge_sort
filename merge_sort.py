INITIAL = 0

class MergeSort:
    def __init__(self):
        pass

    def sorting(self,unsorted_array):
        arr_length = len(unsorted_array)
        if arr_length > 1:
            mid = arr_length//2
            left_half = unsorted_array[:mid]
            right_half = unsorted_array[mid:]
            deep_left = self.sorting(left_half)
            deep_right = self.sorting(right_half)
            return self.merge(deep_left, deep_right, unsorted_array)
        return unsorted_array

    def merge(self, deep_left, deep_right, arr):
        left_counter = right_counter = arr_counter = INITIAL
        while left_counter < len (deep_left) and right_counter < len (deep_right):
            if deep_left[left_counter] > deep_right[right_counter]:
                arr[arr_counter] = deep_right[right_counter]
                right_counter += 1
            else:
                arr[arr_counter] = deep_left[left_counter]
                left_counter += 1
            arr_counter += 1

        while left_counter < len (deep_left):
            arr[arr_counter] = deep_left[left_counter]
            left_counter += 1
            arr_counter += 1

        while right_counter < len (deep_right):
            arr[arr_counter] = deep_right[right_counter]
            right_counter += 1
            arr_counter += 1

        return arr


if __name__ == '__main__' :
    arr = [12,8,5,7,2,8,9,1,2,10]
    merge = MergeSort()
    res = merge.sorting(arr)
    print(res)
