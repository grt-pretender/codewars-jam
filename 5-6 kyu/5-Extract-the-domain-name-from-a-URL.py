# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 

#For example:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"


import re
def domain_name(url):

        pattern = r'^(http://|https://|http://www\.|https://www\.|www\.)(www\.)?'
        domain = re.sub(pattern, "", url).split(".")[0]
        return domain
