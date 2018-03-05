import sys
import random
    
def quicksort(array, leftIndex, rightIndex):
    if leftIndex >= rightIndex:
        return

    # Choose a random pivot
    randIndex = random.randint(leftIndex, rightIndex)
    array[leftIndex], array[randIndex] = array[randIndex], array[leftIndex]
    
    pivotIndex = partition(array, leftIndex, rightIndex)
    
    quicksort(array, leftIndex, pivotIndex - 1)
    quicksort(array, pivotIndex + 1, rightIndex)
    

def partition(array, left, right):
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i-1] = array[i-1], array[left]
    return i-1

            
def main():
    # Read the numbers in the txt file into a list of integers
    with open(sys.argv[1], 'r') as f:
        x = f.readlines()
        array = [int(x[i]) for i in range(1, len(x))]

    # Sort and print the array
    quicksort(array, 0, len(array) - 1) 
    print(array)
    
main()
