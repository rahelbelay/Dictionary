


def check_arrays(array1,array2): 
    for numbers in array1:
        if (numbers ** 2) not in array2 :
            return False
        
    return True   


print(check_arrays([1,2,3,4], [1,4,5,6]))
print(check_arrays([1,2,3,4], [1,4,5,6]))
print(check_arrays([1,2,3,4],[1,4,4,2]))
print(check_arrays([1,2,3,4,5],[1,2,3,4]))


