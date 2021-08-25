# YOUR NAME HERE
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
        # Equal to 1 since the heap list was initialized with a value
        if len(self.data) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        root = self.data[1]
 
        # Move the last value of the heap to the root
        self.data[1] = self.data[self.size]
 
        # Pop the last value since a copy was set on the root
        *self.data, _ = self.data
 
        # Decrease the size of the heap
        self.size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.heapify_down(1)
 
        # Return the min value of the heap
        return root 
            
            
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    def heapify_up(self, item):
        curr = self.size + 1
        self.data.append(item)
        # print("*****************\nAt the start our data is this: %s" %self.data)
        while (curr > 1 and self.data[curr] < self.data[curr // 2]):
            # print("Flipping %s and %s" % (self.data[curr], self.data[curr // 2]))
            self.swap(curr, curr // 2)
            #print("The array is now: %s" % self.data)
            curr = curr // 2
    
    def heapify_down(self, item):
        
        while (item * 2) <= self.size:
            # Get the index of the min child of the current node
            mc = self.min_child(item)
            # Swap the values of the current element is greater than its min child
            if self.data[item] > self.data[mc]:
                self.data[item], self.data[mc] = self.data[mc], self.data[item]
            item = mc
    
    def min_child(self, i):
      
        if (i * 2)+1 > self.size:
            return i * 2
        else:
           
            if self.data[i*2] < self.data[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1

    def __str__(self):
        # return "%s" % self.data
        result = ""
        count = 2
        for i in range(1, len(self.data)):
            if i == count:
                count *= 2
                result += " "
            result += "%s\t" % self.data[i]
        return result


def main():
    print("Welcome to the heap code!")
    my_heap = MinHeap()
    
    my_heap.insert(6)
    print(my_heap)
    my_heap.insert(2)
    print(my_heap)
    my_heap.insert(7)
    print(my_heap)
    my_heap.insert(4)
    print(my_heap)
    my_heap.delete_min()
    print(my_heap)
    my_heap.insert(5)
    print(my_heap)
    my_heap.insert(9)
    print(my_heap)
    my_heap.delete_min()
    print(my_heap)
    my_heap.insert(3)
    print(my_heap)
    my_heap.insert(1)
    print(my_heap)
    my_heap.delete_min()
    print(my_heap)

    
    """
    my_heap2 = MinHeap()
    print("\nLet us now add random numbers to our min heap and verify the performance")
    to_add = []
    for i in range(31):
        to_add.append(random.randint(0,100))
        
    print(to_add)
    print("Now that we have generated a random array of ints, let us add themn to the min-heap")
        
    for item in to_add:
        my_heap2.insert(item)
        
    print(my_heap2)
    """


main()