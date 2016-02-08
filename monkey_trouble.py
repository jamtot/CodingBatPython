# We have two monkeys, a and b, and the parameters 
# a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or 
# if neither of them is smiling. Return True if we are in trouble. 

def monkey_trouble(a_smile, b_smile)
    # if both are either smiling or not    
    if a_smile == b_smile:
        # we are in trouble D:
        return True
    # if only one is smiling
    else:
        # we're ok :D
        return False

# can be shortened to 
# return (a_smile == b_smile)
