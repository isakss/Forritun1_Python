def remove_evens(list_object):
    for element in reversed(list_object):
        if element % 2 == 0:
            list_object.remove(element)
    return list_object

def remove_evens2(list_object):
    new_list = []
    for element in list_object:
        if element % 2 != 0:
            new_list.append(element)
    return new_list
# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)