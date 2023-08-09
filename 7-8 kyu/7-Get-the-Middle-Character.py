# You are going to be given a word. 
# Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

# Solution:

def get_middle(s):
    
    for char in s:
        index = int(len(s) / 2)

        if len(s) == 1:
            return s
        elif len(s) % 2 != 0:
            return s[index]
            
        else:
            return s[index - 1 : index + 1]
   

test = get_middle("middle")
print(test)