def insertionSort(array):

    # O(1)- space, O(n*2) - time complexity, where n = lenght of array

   for i in range(1, len(array)):

       j = i

       while j > 0 and array[j] < array[j-1]:
           swap(j, j-1, array)

           j -= 1

   return array


def swap(i, j, array):

    array[i], array[j] = array[j], array[i]