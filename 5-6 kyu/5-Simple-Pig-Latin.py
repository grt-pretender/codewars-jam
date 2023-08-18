# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples:
# pig_it('Pig latin is cool') - igPay atinlay siay oolcay
# pig_it('Hello world !')     - elloHay orldway !

import re

def pig_it(text):
    text = text.split(" ")
    pattern = r"!.,%&#()?"
    new_text = ""

    for w in text:

        if w in pattern:
            new_text = new_text + w
        else:
            new_w = w[1:] + w[0] + "ay"
            new_text += new_w + " "

    return new_text.strip()
