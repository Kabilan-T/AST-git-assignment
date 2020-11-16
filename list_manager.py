# List manager

def random_order(list):
    random = np.random.shuffle(my_list)
    return random

def order_by_increasing_value(list):
    list.sort() 
    return list
    

def order_by_decreasing_value(list):
    descend = np.sort(my_list)[: : -1]
    return descend

def reverse_order(list):
    reverse = np.flip(my_list)
    return reverse

def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    stringfy_list = [str(i) for i in list]
    return stringfy_list
    #pass

def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    multiply_list = [i*multiple for i in list]
    return multiply_list
    #pass

def get_highest_value(list):
    '''returns the highest value of the list'''
    list.sort() 
    return list[-1:]
    #pass

def get_lowest_value(list):
    '''returns the lowest value of the list'''
    list.sort() 
    return list[:1]
    #pass