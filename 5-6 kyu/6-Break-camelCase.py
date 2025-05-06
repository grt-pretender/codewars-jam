# Complete the solution so that the function will break up camel casing, using a space between words:
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


# ================
# 1) Using regex
# ================

import re
def solution(s):
  break_camelcase = re.sub( r"([A-Z])", r" \1", s).split()
  ans = " ".join(break_camelcase)
  return ans


# ================
# 2) Using a new string
# ================

def solution(s):
    ans = ""
    for c in s:
        if c.isupper():
            ans += " "
        ans += c
    return ans