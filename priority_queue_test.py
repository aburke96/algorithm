# Alexandra Burke
# heap.py
# 3/15/21
# This program contains implementation for a basic heap structure.
# We will expand on this for in class practice and for the homework
# A heap is a semi sorted datastructure that gives us instant access 
# to the item of most priority in the structure, typically the minimal
# or maximal value. This implementation is for min-heaps.

import random

class MinHeap:
	
    def __init__(self):
        self.size = 0
        self.data = [None]
    
    def peak(self):
        if self.size > 0:
            return self.data[1]
        else:
            return None
    
    def insert(self, item):
        if self.size == 0:
            self.data.append(item)
            self.size += 1
        else:
            self.heapify_up(item)
            self.size += 1
            
    def delete_min(self):
        if self.size == 0:
            return self.data[self.size]
        minItem = self.data[1]
        self.swap(1, self.size) 
        self.size = self.size - 1
        self.data.pop()
        self.heapify_down()
        return minItem

            
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    # Heapify up is used when we insert a new element to a heap. 
    # When inserting a new element, we add it at the bottom of the heap tree, and move up 
    # the tree while comparing to the current parent element and swapping if needed
    def heapify_up(self, item):
        curr = self.size + 1
        self.data.append(item)
        #print("*****************\nAt the start our data is this: %s" % self.data)
        while (curr > 1 and self.data[curr] < self.data[curr // 2]):
            #print("Flipping %s and %s" % (self.data[curr], self.data[curr // 2]))
            self.swap(curr, curr // 2)
            #print("The array is now: %s" % self.data)
            curr = curr // 2
    
    # Heapify down is used when we remove the top element from a heap. 
    # Removal of an element is done by swapping the top element with the last element at the bottom of the tree,
    # removing the last element, and then heapfying the new top element down to maintain the heap property. 
    # Because this moves down the heap tree, it must perform two comparisons per iteration, 
    # with the left child and the right child elements, then swap with the smaller one.
    def heapify_down(self):
        curr = 1
        while(curr < self.size):
            smallest = curr
            left = 2*curr
            right = 2*curr + 1
            if (left < self.size and self.data[left] < self.data[curr]):
                smallest = left

            if (right < self.size and self.data[right] < self.data[curr] and self.data[right] < self.data[left]):
                smallest = right

            if (smallest != curr):
                self.swap(curr, smallest)
                curr = smallest
            else:
                break


    # This function will subtract the value of the min element 
    # (the one being removed) and subtract it from all entries in the heap.
    def decremenet_all(self, val):
        newdata = []
        for i in range(1, len(self.data)):
            newdata.append(self.data[i] - val)
        self.data = [None] + newdata
        #print(self)
        while(self.peak() == 0):
            self.delete_min()
    
    def __str__(self):
        # return "%s" % self.data
        result = ""
        count = 2
        for i in range(1, len(self.data)):
            if i == count:
                count *= 2
                result += "\n"
            result += "%s\t" % self.data[i]
        return result


def main():
    print("Welcome to the test code for heaps!")
    print("Our first calls will fill the heap, and then we will remove the min value several times")
    print("Afterwards we shall have a test of decrement-all")
    print("Finally you will engage in the teller simulation")
    print("This teller simulation may take the form of a loop here in main OR a method which will be called")
    my_heap = MinHeap()
   
    my_heap.insert(7)
    my_heap.insert(9)
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(12)
    my_heap.insert(4)
    my_heap.insert(14)
    my_heap.insert(10)
    my_heap.insert(6)
    my_heap.insert(3)
    print(my_heap)
    # The results of the heap should be the following
    # 3
    # 3       4
    # 6       5       7       14
    # 10      9       12
    
    print("Now for removal")
    my_heap.delete_min()
    print(my_heap)
    # After removal one, 12 is rotated to root, swapped with 3, and then 5. 5 has no children so the rotation ends
    # 3
    # 5       4
    # 6       12      7       14
    # 10      9
        
    my_heap.delete_min()
    print(my_heap)
    # After removal two, 9 is rotated to root, swapped with 4, swapped with 7. 7 has no children so the rotation ends
    # 4
    # 5       7
    # 6       12      9       14
    # 10
    
    my_heap.delete_min()
    print(my_heap)
    # After removal three, 10 is rotated to root, swapped with 5, swapped with 6
    # 5
    # 6       7
    # 10      12      9       14
    
    
    print('Now to add four values of 2 and three of 7 to demonstrate the power of decremenet_all')
    my_heap.insert(2)
    my_heap.insert(2)
    my_heap.insert(7)
    my_heap.insert(2)
    my_heap.insert(2)
    my_heap.insert(7)
    my_heap.insert(7)
    print(my_heap)
    # HEre is what the heap should be after the above deletions
    # 2
    # 2       2
    # 5       2       7       7
    # 10      6       12      7       9       7       14
    tmp = my_heap.delete_min()

    print(my_heap)
    my_heap.decremenet_all(tmp)
    # After a call of delete min and then decrement all, this is our heap
    # 3
    # 4       5
    # 5       5       7       5
    # 8       12      10
    print('\n\n%s' % my_heap)
    tmp = my_heap.delete_min()
    my_heap.decremenet_all(tmp)
    print('\n\n%s' % my_heap)
    # After a second delete min (removing 3) our heap now looks like this
    # 1
    # 2       2
    # 5       2       4       2
    # 7       9
    
    # Now run the simulation. As a reminder, your simulation will have X number of tellers
    # and an input array of wait times. You will load X items from the array into the heap
    # Then perform delete-min and decrement all. Then refill the heap to size X and repeat until 
    # all items from the array have passed through the array.
    # If our heap size is 5, and our array is [1,1,5,2,2,3,1], we get the following as the original heap
    # 1
    # 1 5
    # 2 2
    # After delete-min and decrementing, we have the following heap
    # 1
    # 1 4
    # When we load 3 and 1 in, the heap becomes
    # 1
    # 1 4
    # 3 1
    # Delete and decrement gives us
    # 2
    # 3
    # We delete and decrement 2, leaving us with 1 remaining in the heap, then delete and finish
    print("_______________")
    a = [1,1,5,2,2,3,1]
    my_heap = MinHeap()
    for i in range(5):
        my_heap.insert(a.pop(0))

    print(my_heap)

    print("_______________")

    temp = my_heap.delete_min()
    my_heap.decremenet_all(temp)

    print(my_heap)

    print("_______________")

    my_heap.insert(1)
    my_heap.insert(3)

    print(my_heap)

    print("_______________")

    temp = my_heap.delete_min()
    my_heap.decremenet_all(temp)

    print(my_heap)

    print("_______________")

    temp = my_heap.delete_min()
    my_heap.decremenet_all(temp)    

    print(my_heap)

main()