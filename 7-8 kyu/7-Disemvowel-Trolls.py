# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels 
# from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string 
# and return a new string with all vowels removed.

# For ex, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


# 1) one solution:

import re
def disemvowel(string_):
	vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
	for s in string_:
		if s in vowels:
			string_ = string_.replace(s, '')
	return string_



# 2) using regex

import re
def disemvowel(string_):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, "", string_)



# 3) using new string

def disemvowel(string_):
	store = ""
	pattern = "aeiou"
    for s in string_:
        if s.lower() not in pattern:
            store += s
    return store

