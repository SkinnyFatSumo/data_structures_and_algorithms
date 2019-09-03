'''MERGE SORT'''
def mergeSort(array):

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)
        i=j=k=0
       
        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                array[i] = left[j]
                j += 1
            else:
                array[i] = right[k]
                k += 1
            i += 1
       
        while j < len(left):
            array[i] = left[j]
            i += 1
            j += 1

        while k < len(right):
            array[i] = right[k]
            i += 1
            k += 1
    
    return array


'''MERGE SORT __ COMMENTED'''
# takes an array of integers as input
# NOTE: - this array is mutable and the original WILL be altered
#       - because it's called recursively, we can't copy it within the function
#       - so to preserve the original, it must be copied prior to function call
def mergeSort__Commented(array):
    # if array is only 1 item long, it's sorted, no need to do anything
    # if longer than 1 item, split into 2 subarrays for sorting
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # recursively call sorting function
        mergeSort(left)
        mergeSort(right)

        # initialize index of sub-arrays and combined array to 0 (lowest index)
        i=j=k=0
       
        # we know array left and right are sorted, because of recusrive merges

        # while both sub arrays have values, take each of their lowest values
        # and append the lower of the two to the merging array
        # then increment the index on the sub array from which the value 
        # was taken in order to remove that value from the pool
        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                array[i] = left[j]
                j += 1
            else:
                array[i] = right[k]
                k += 1
                # also increment index of merged array
            i += 1
       
        # if only the left array remains, run through it appending values
        # to and incrementing index of merged array
        while j < len(left):
            array[i] = left[j]
            i += 1
            j += 1

        # same as above, but for right side
        while k < len(right):
            array[i] = right[k]
            i += 1
            k += 1

    return array


original_array = [1, 3, -2, 2, 19, 8, -5, 0, 11, 21, 4]
input_array = original_array[:]
merge_sorted_array = mergeSort(input_array)

print('original:       ' + str(original_array) + '\n')
print('merge sorted:   ' + str(merge_sorted_array) + '\n')
