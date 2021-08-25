# ALEXANDRA BURKE
# inclass_three.py
# 3/8/21
# In this program we will experiment with the idea of multisorting
# Multisorting is a process by which we sort a complex dataset repeatedly by different attributes
# When performing a multisort we care about the stability of the data (tied items preserve prior order)
# For this practice you will need to modify the base sorting algorithm to work with complex data.
# By default, the data is read in from file, broken into an array, and loaded into another array. 
# This gives us a two dimensional array. The interior arrays are composed of the following:
# [first_name, last_name, major, age, GPA]
# You will modify the stable sorting algorithm of your choice to work with this 2-D array
# (all sorts from basic_sorts.py are included)
# Reminder that we must use a stable sort, and that we must be able to select the attribute that 
# is to be sorted upon.

def main():
    in_name = "large_student_list.txt"



    try:
        my_data = []
        in_file = open(in_name)
        for line in in_file:
            tmp = line.split('\t')
            my_data.append([tmp[0], tmp[1], tmp[2], int(tmp[3]), float(tmp[4])])


        in_file.close()
        



    except IOError:
        print("There was an error reading the file!")

    # We complete the rest of the program after the try/except block
    for item in my_data:
        print(item)
    print("Below this print statement place multiple calls to the sorting method you modify")
    print("As an example, have bubblesort be called on first name, last name, major")
    print("Or insertion sort on age, last name, gpa")

    bubbleSort(my_data, [2,0,1,3,4])

    
        



# Bubblesort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.
def bubbleSort(my_array0, col): 
    n = len(my_array0) # operation

    if(len(col) != 5):
        print("please specify column order for all columns")
        return
    my_array = []
    for r in my_array0:
        string = str(r[col[0]]) + "\t" + str(r[col[1]]) + "\t" + str(r[col[2]]) + "\t" + str(r[col[3]]) + "\t" + str(r[col[4]])
        my_array.append(string)

    # Traverse through all array elements 
    for i in range(n): # instantiation of a loop is 2-4, every iteration is 2
        swapped = False
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if my_array[j] > my_array[j+1]: 
                # print("Swapping items %s and %s" % (my_array[j], my_array[j+1]))
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        
        if (not swapped):
            break
    my_array1 = []
    for r in my_array:
        item = r.split("\t")
        i0 = findIndex(0, col)
        i1 = findIndex(1, col)     
        i2 = findIndex(2, col)
        i3 = findIndex(3, col)
        i4 = findIndex(4, col)
        item0 = [item[i0],item[i1],item[i2],item[i3],item[i4]]
        my_array1.append(item0)
    for r in my_array1:
        print(r)

def findIndex(i, arr):
    num = 0
    for x in range(len(arr)):
        if(i == arr[x]):
            return num
        num = num + 1


# Selectionsort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.
def selectionSort(my_array, col):
    # Traverse through all array elements 
    for i in range(len(my_array)):  
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(my_array)): 
            if my_array[min_idx][col[0]] > my_array[j][col[0]]: 

                min_idx = j
                # print("Min_index reassigned")

        # Swap the found minimum element with  
        # the first element       
        # print("Swapping %s into slot %d" % (my_array[min_idx], i))
        my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]
    print("--------------------------------")
    
    

# Insertionsort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.
def insertionSort(my_array): 
    # Traverse through 1 to len(my_array) 
    for i in range(1, len(my_array)): 
  
        key = my_array[i] 
        # print("We are looking to correctly place %d into our array! It is currently the %d element" % (key, i))
        # Move elements of my_array[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < my_array[j] : 
                # print("Swapping %s with %s" % (key, my_array[j]))
                my_array[j + 1] = my_array[j] 
                j -= 1
        my_array[j + 1] = key 
        res = ""
        for k in range(0,i+1):
            res += "%s " % my_array[k]
        # print("Our current sorted list is: %s" % res)


# Shellsort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.
# Shellsort's efficiency depends on the gap sequence, and the method in which it changes.
# Feel free to edit the gap sequence and its reduction
def shellSort(my_array): 
    # Start with a big gap, then reduce the gap 
    n = len(my_array) 
    gap = n//2 # Guarantees an integer result
    # print("Starting gap sequence is %d" % gap)
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
        for i in range(gap,n): 
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = my_array[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and my_array[j-gap] >temp: 
                my_array[j] = my_array[j-gap] 
                # print("Swapping %s and %s" % (my_array[j], temp))
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            my_array[j] = temp 
        gap //= 2
        # print("Our new gap sequence is %d" % gap)
        # print(my_array)


# Mergesort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.
def mergeSort(my_array): 
    if len(my_array) > 1: 
        mid = len(my_array)//2 #Finding the mid of the array 
        L = my_array[:mid] # Dividing the array elements (grabs allelements until mid)  
        R = my_array[mid:] # into 2 halves 
        # print(L)
        # print(R)

  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        # Continues until array of size 1
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            # print("Comparing %s to %s" % (L[i], R[j]))
            if L[i] < R[j]: 
                my_array[k] = L[i] 
                i+=1
            else: 
                my_array[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L):
            # print("Adding %s to the array" % L[i])
            my_array[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            # print("Adding %s to the array" % R[j])
            my_array[k] = R[j] 
            j+=1
            k+=1
        # print(my_array)


# Partition
# Helper method for quicksort
def partition(my_array,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = my_array[high]     # pivot 
    # print("We are using %s as the pivot" % pivot)
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   my_array[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1
            # print("Swapping %s with %s, moving %s before the pivot" % (my_array[j], my_array[i], my_array[j]))            
            my_array[i],my_array[j] = my_array[j],my_array[i] 
  
    my_array[i+1],my_array[high] = my_array[high],my_array[i+1] 
    return ( i+1 ) 
  
  
# Quicksort
# Precondition: The input my_array is an array of Comparable elements.
# Postcondition: The Comparable data inside my_array will be placed in sorted order.  
def quickSort(my_array,low,high): 
    if low < high: 
  
        # pi is partitioning index, my_array[p] is now 
        # at right place 
        pi = partition(my_array,low,high)
        # print("After partitioning, our array is currently:\n%s" % my_array)
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(my_array, low, pi-1)
        # print("After recursive call one, our array is now:\n%s" % my_array)
        quickSort(my_array, pi+1, high) 
        # print("After recursive call two, our array is now:\n%s" % my_array)


main()