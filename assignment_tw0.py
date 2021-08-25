# Anna Burke
# COSC 2316
# 3/4/21
# Assignemnt 2

# This class contains implementation of an array stack.
class Stack():
	
	# Declares an initially empty stack 
	def __init__(self):
		self.size = 0
		self.stack = []
	
	# Pushes an item to the top of the stack
	def push(self, item):
		self.stack.append(item)
		self.size += 1
		
	# Removes the top item from the stack
	def	pop(self):
		if (self.size <= 0):
			print("You are attempting to delete from an empty stack.")
			print("In a proper code environment we would throw an exception here")
		else:
			self.size -= 1
			return self.stack.pop()
	
	# Returns the top item of the stack (without removing it)
	def peek(self):
		if (self.size == 0):
			print("Currently the stack is empty!")
		else:
			print("The top item of the stack is currently: %s" % self.stack[self.size-1])
	
	# Returns the size of the stack
	def get_size(self):
		return self.size
		
	# Tostring method for the stack
	def __str__(self):
		result = ""
		for i in range(len(self.stack)):
			result += "Item %d: %s\n" % ((i + 1), self.stack[i])
		
		return result




# Describe your change making algorithm here (what are the units)
def change_one_american(amount):
    quarters = 0
    dimes = 0 
    nickels = 0 
    pennies = 0
    while(amount >= 25):
        amount = amount - 25
        quarters += 1
    
    while(amount >= 10):
        amount = amount - 10
        dimes += 1
    
    while(amount >= 5):
        amount = amount - 5
        nickels += 1
    
    while(amount >= 1):
        amount = amount - 1
        pennies += 1
    
    return "quarter = " + str(quarters) + " dimes = " + str(dimes) + " nickels = " + str(nickels) + " pennies = " + str(pennies)

def change_one(amount):

    six = 0 
    ten = 0 
    ones = 0
    while(amount >= 10):
        amount = amount - 10
        ten += 1

    while(amount >= 6):
        amount = amount - 6
        six += 1
    


    while(amount >= 1):
        amount = amount - 1
        ones += 1
    
    return " ten= " + str(ten) + " six = " + str(six) + " ones = " + str(ones)


# Describe your change making algorithm here (what are the units) 
def change_two(amount):
    ones = 0
    fours = 0 
    fives = 0 
    while(amount >= 5):
        amount = amount - 5
        fives += 1
    
    while(amount >= 4):
        amount = amount - 4
        fours += 1
    
    while(amount >= 1):
        amount = amount - 1
        ones += 1
    return "fives = " + str(fives) + " fours = " + str(fours) + " ones = " + str(ones) 


# Describe your balance checking algorithm here    
def balance_check(string):
    S = Stack()
    for char in string:
        if char == '(':
            S.push(char)
        elif char == ')':
            # if size is 0 we can't match )
            if S.size == 0:
                return False
            S.pop()
    # if we have items in stack we didn't match
    if S.size != 0:
        return False
    return True

# Describe your balance checking algorithm here    
def balance_check_bonus(string):
    S = Stack()
    for char in string:
        if char == '(' or char == '[' or char == '{':
            S.push(char)
        elif char == ')':
            if S.size == 0:
                return False
            last = S.pop()
            if last != '(':
                return False
        elif char == ']':
            if S.size == 0:
                return False
            last = S.pop()
            if last != '[':
                return False
        elif char == '}':
            if S.size == 0:
                return False
            last = S.pop()
            if last != '{':
                return False
    # if we have items in stack we didn't match
    if S.size != 0:
        return False
    return True


def main():
    print("Welcome to assignment #2!")
    print("Presented below are two algorithms, one for change making and one for balance checking")
    
    
    print("-------------------------")
    print("Change making algorithm one:")
    print("The results of calling change_one with input 40 is: %s" % change_one(40))
    print("The results of calling change_one with input 20 is: %s" % change_one(20))
    print("The results of calling change_one with input 14 is: %s" % change_one(14))
    print("The results of calling change_one with input 13 is: %s" % change_one(13))
    
    print("\n-------------------------")
    print("Change making algorithm two:")
   
    print("The results of calling change_two with input 4 is: %s" % change_two(4))
    print("The results of calling change_two with input 6 is: %s" % change_two(6))
    print("The results of calling change_two with input 8 is: %s" % change_two(8))
    print("The results of calling change_two with input 12 is: %s" % change_two(12))
    

    print("\n-------------------------")
    print("Balance checking algorithm")
    print("The results of calling balance_check on ((())) is: %s" % balance_check("((()))"))  # TRUE
    print("The results of calling balance_check on (()()(())) is: %s" % balance_check("(()()(()))")) # TRUE
    print("The results of calling balance_check on ((()()()()) is: %s" % balance_check("((()()()())")) # FALSE
    print("The results of calling balance_check on ()(())((()()))) is: %s" % balance_check("()(())((()())))")) #FALSE

    print("\n-------------------------")
    print("Bonus checking algorithm")
    print("The results of calling balance_check on ((())) is: %s" % balance_check_bonus("({[]})"))  # TRUE
    print("The results of calling balance_check on (()()(())) is: %s" % balance_check_bonus("({[}])")) # FALSE

main()