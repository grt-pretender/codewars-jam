# In this kata, you have an input string 
# and you should check whether it is a valid message. 

#You need to split the string by the numbers, 
# and then compare the numbers with the number of characters in the following substring.

# Examples:
# 1) "3hey5hello2hi", the result is true.
# 2) "hello5" and "2hi2" are invalid.

# Notes:
# Messages are composed of only letters and digits.
# Numbers may have multiple digits: e.g. "4code13hellocodewars" is a valid message.
# Every number must match the number of character in the following substring, otherwise the message is invalid.
# If the message is an empty string, you should return true.


import re
def is_a_valid_message(message):
    
    pattern = re.compile(r'(\d+)(\D+|$)')
    matches = re.findall(pattern, message)
    
    for match in matches:
        if len(match[1]) != int(match[0]):
            return False
    return True

