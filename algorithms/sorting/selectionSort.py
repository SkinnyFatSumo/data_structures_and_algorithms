'''SELECTION SORT'''
def selectionSort(passed_array):
    array = passed_array[:]

    for i in range(0, len(array) - 1):
        smallest = i 
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
    
    return array


'''SELECTION SORT __ COMMENTED''' 
def selectionSort__Commented(passed_array):
    # copy to preserve original
    array = passed_array[:]

    # for every value in the array, except last
    for i in range(0, len(array) - 1):
        # the first value is the smallest so far, store its index
        smallest = i 
        # go through rest of area looking for the actual smallest number
        # and store it's index
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                # remember index of smallest number
                smallest = j
        # swap actual smallest number and number at index i
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp

    return array
        
my_array = [1, 3, -2, 2, 19, 3, 8, -5, 0, 19, 11, 21, 4]
print(selectionSort(my_array))
