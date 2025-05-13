# Write a function that takes an array of words 
# and smashes them together into a sentence and returns the sentence. 

# You can ignore any need to sanitize words or add punctuation, 
# but you should add spaces between each word. 

# Be careful, there shouldn't be a space at the beginning or the end of the sentence!


# ==========================
# 1) One solution
# ==========================

def smash(words):
    return " ".join(words) 


# ==========================
# 2) And another one
# ==========================

def smash(words):
    result = ""
    for w in words:
        result += str(w) + " "
    ans = result[:-1]
    return ans
