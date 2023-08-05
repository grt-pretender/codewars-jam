# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# 1) solution

def get_count(sentence):
	
	vowels = ["a", "e", "i", "o", "u"]
	counter = 0
	for v in sentence:
		if v in vowels:
			counter += 1

	return counter

# 2) using regex

import re
def get_count(sentence):
	count = len(re.findall('[aeiou]', sentence))
    return count

