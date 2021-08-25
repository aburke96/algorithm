# Dr Michaels
# radix.py
# 3/22/2021
# This program contains multiple implementations of LSD Radix Sort
# We will walk through together the formation of MSD Radix 

import random

# This method contains the LSD radix sort implementation that uses
# modulus and division to place the numbers.
# This method does not require padding
def radix_one(data, longest):
    current_order = make_num_dict()
    prev_order = {}
    mod_val = 10
    div_val = 1
    digit = 1
    while (digit <= longest):
        if digit == 1:
            for item in data:
                place = item % mod_val
                current_order[place].append(item)
        else:
            for key in prev_order:
                for item in prev_order[key]:
                    place = (item % mod_val) // div_val
                    current_order[place].append(item)
        prev_order = current_order
        current_order = make_num_dict()
        digit += 1
        mod_val *= 10
        div_val *= 10
        
    count = 0
    for key in prev_order:
        for item in prev_order[key]:
            data[count] = item
            count += 1
    

# This radix sort will work with string characters.
# It will use LSD radix sort
# It implies padding by having a bucket for "no character"
# It will cast the character being analyzed as lower case
def radix_two(data, longest):
    current_order = make_char_dict()
    prev_order = {}

    curr = longest - 1
    while curr >= 0:
        if curr == (longest - 1):
            for item in data:
                the_char = item[curr:curr+1].lower()
                current_order[the_char].append(item)
        else:
            for key in current_order:
                for item in prev_order[key]:
                    the_char = item[curr:curr+1].lower()
                    current_order[the_char].append(item)
        curr -= 1
        prev_order = current_order
        current_order = make_char_dict()
    count = 0
    for key in prev_order:
        for item in prev_order[key]:
            data[count] = item
            count += 1


	
# This will MSD sort integers. We need an input of the largest datapoitns	
def radix_msd(data, longest):

    current_order = make_num_dict()
    prev_order = {}
    mod_val = 10
    div_val = 1
    digit = 1
    while (digit <= longest):
        if digit == 1:
            for item in data:
                place = item % mod_val
                current_order[place].append(item)
        else:
            for key in prev_order:
                for item in prev_order[key]:
                    place = (item % mod_val) // div_val
                    current_order[place].append(item)
        prev_order = current_order
        current_order = make_num_dict()
        digit += 1
        mod_val *= 10
        div_val *= 10
        
    count = 0
    for key in prev_order:
        for item in prev_order[key]:
            data[count] = item
            count += 1
    

def make_num_dict():
    my_data = {}
    for i in range(10):
        my_data[i] = []
    return my_data

def make_num_dict2():
    my_data = {}
    for i in range(10):
        my_data['%s' % i] = []
    return my_data

def make_char_dict():
    the_chars = 'abcdefghijklmnopqrstuvwxyz'
    my_data = {}
    my_data[''] = []
    for char in the_chars:
        my_data[char] = []
    return my_data

def is_sorted(my_data):
    for i in range(len(my_data) - 1):
        if my_data[i] > my_data[i+1]:
            return False
    return True
    
def get_longest(my_data):
    long_string = 0
    for item in my_data:
        if len(item) > long_string:
            long_string = len(item)
    return long_string

def main():
    print("This will test radix sort!")
    print("Our first test will be small, the second test will be with 1000 integers")
    print("A similar test will be conducted with strings.")
    test_one = [512, 123, 908, 142, 98, 1000, 542, 7, 5000]
    radix_one(test_one, 4)
    print(test_one)
    
    test_two = []
    for i in range(1000):
        test_two.append(random.randint(0,99999))
    
    radix_one(test_two, 5)
    print("The data in the randomized test array is sorted: %s" % is_sorted(test_two))
    
    # print("\nNow let us test strings!")
    #test_three = ['alpha', 'zeta', 'omega', 'Gamma', 'bETA', 'Epsilon', 'easter', 'ACE']
    #radix_two(test_three, 7)
    #print(test_three)
    # print('We will now make 1000 random strings of random length and capitalizations')
    
    # the_chars = 'abcdefghijklmnopqrstuvwxyz'
    # test_four = []
    # for i in range(1000):
        # j = 1
        # tmp = ''
        # while j > 0.1:
            # cap = random.random()
            # if cap > 0.8:
                # tmp += the_chars[random.randint(0,25)].upper()
            # else:
                # tmp += the_chars[random.randint(0,25)]
            # j = random.random()
        # test_four.append(tmp)
        
    # radix_two(test_four, get_longest(test_four))
    # for item in test_four:
        # print(item)
        
    # print("We will now test msd radix")
    test_five = [123, 127, 121, 12, 108, 1008, 900, 1076, 2100, 5999, 8]
    radix_msd(test_five, 4)
    print(test_five)
    
    # test_six = []
    # for i in range(1000):
        # test_six.append(random.randint(0,99999))
    
   




main()