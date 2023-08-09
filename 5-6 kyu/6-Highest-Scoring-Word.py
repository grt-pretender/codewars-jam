# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: 
# a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.


# 1) one solution:

def high(x):
    x = x.split()
    highest_score = 0
    highest_scoring_word = ''

    for curr_word in x:
        curr_score = sum([ord(char) - 96 for char in curr_word])
        if curr_score > highest_score:
            highest_score = curr_score
            highest_scoring_word = curr_word

    return highest_scoring_word


# 2) shorter one:

    def high(x):
        x = x.split()
        our_key = lambda word: sum(ord(char) - 96 for char in word)
        return max(x, key=our_key)


test = high('take me to semynak')
print(test)