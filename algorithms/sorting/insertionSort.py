
'''ASCENDING ORDER'''
def insertionSortAscending(passed_array):
    array = passed_array[:]
    
    for latest in range(1, len(array)):
        key = array[latest]
        so_far = latest - 1

        while so_far >= 0 and array[so_far] > key:
            array[so_far + 1] = array[so_far]
            so_far -= 1
        array[so_far + 1] = key

    return array


'''DESCENDING ORDER'''
def insertionSortDescending(passed_array):
    array = passed_array[:]
    for latest in range(1, len(array)):
        key = array[latest]
        so_far = latest - 1

        while so_far >= 0 and array[so_far] < key:
            array[so_far + 1] = array[so_far]
            so_far -= 1
        array[so_far + 1] = key

    return array


'''ASCENDING ORDER __ COMMENTED'''
# Take array as input and sort it in ascending order
def insertionSortAscending__Commented(passed_array):
    # duplicate array to preserve original
    array = passed_array[:]
    # the index 'latest' will be compared with all indexes to its left
    # begin with latest at index 1, so it has only one on lower index,
        # which is sorted because it's of length 1
    # iterate over the rest of the list
    for latest in range(1, len(array)):
        # current key is value at latest index
        key = array[latest]
        # index to compare against first, is directly to left
        # it represents the last of the array elements sorted 'so_far'
        so_far = latest - 1

        # so long as our key has a value to it's left
        # and that value is greater than it's own
        while so_far >= 0 and array[so_far] > key:
            # insert key into the position of the element it's compared to
            # this mean we are pushing that element to the right
            # it's a swap
            array[so_far + 1] = array[so_far]
            # now decrement index to compare against the last element we haven't
            # yet checked in the sub_array that's sorted
            so_far -= 1
        # if while loop breaks, we've gone beyond the beginning 
        # or found a lesser value at the index of so_far
        # so assign the key to one greater than the index_of so far
        array[so_far + 1] = key

    return array


'''DESCENDING ORDER __ COMMENTED'''
def insertionSortDescending__Commented(passed_array):
    array = passed_array[:]
    for latest in range(1, len(array)):
        key = array[latest]
        so_far = latest - 1

        # instead only continue if the array_so far value is less than the key
        while so_far >= 0 and array[so_far] < key:
            array[so_far + 1] = array[so_far]
            so_far -= 1
        array[so_far + 1] = key

    return array


my_array = [1, 3, -2, 2, 19, 8, -5, 0, 11, 21, 4]

ascending_sorted_array = insertionSortAscending(my_array)
descending_sorted_array = insertionSortDescending(my_array)

print('original:  ' + str(my_array) + '\n')
print('ascending:  ' + str(ascending_sorted_array) + '\n')
print('descending:  ' + str(descending_sorted_array) + '\n')
