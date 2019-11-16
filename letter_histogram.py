
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

# enter words input
# count letters
# add same letters
# return out put
user_input = input("please enter a word:")


def letter_histogram (user_input):
    
    new_dict = {}
    for letter in user_input:
        ['letter'][0]=1
        new_dict[letter]= 1
        
        
        if  letter in new_dict:
            return new_dict
print(letter_histogram(user_input))

