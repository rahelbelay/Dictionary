
# *THIS SHOULD BE SOLVED USING DICTIONARIES!


# *YOU MAY NOT CHECK IF THE ARRAYS ARE EQUAL. THIS METHOD *DOES* WORK IN


# *PYTHON, BUT NOT IN JAVASCRIPT. THE EXERCISE IS TO PRACTICE USING


# *DICTIONARIES AND FREQUENCY PATTERNS

# Create a function that accepts two strings and checks if they are valid anagrams.
 

# Examples
# "pie", "eip" = true
# "pie", "pie" = true
# "pie", "pies" = false
# "pie", "pwe" = false


def my_string (word1,word2):
    if len(word1)!= len(word2):
        return False

    for word in word1:
        if word1 not in word2:
            return False
    return True
print(my_string("pie", "eip"))
print(my_string("pie", "pie"))
print(my_string("pie", "eips"))
print(my_string("pie", "pwe"))
    
    
        

