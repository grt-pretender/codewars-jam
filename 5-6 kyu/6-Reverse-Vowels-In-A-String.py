# In this kata, your goal is to write a function which will reverse the vowels in a string. 
# Any characters which are not vowels should remain in their original position. 
# For simplicity, you can treat the letter y as a consonant, not a vowel.

# Here are some examples:

# "Hello!" => "Holle!"
# "Tomatoes" => "Temotaos"

# Solution:

def reverse_vowels(s):

    pattern = 'aeoiuAEOIU'
    vowels = [char for char in s if char in pattern]

    new_string = ""
    index = 0

    for char in s:
        if char in pattern:
            new_string += vowels.pop()
            index += 1

        else:
            new_string += char
            
    return new_string




test = reverse_vowels("Reverse Vowels In A String")
print(test)