// You will be given a list of strings. 
// You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) 
// and then return the first value.
// The returned value must be a string, and have "***" between each of its letters.
// You should not remove or add elements from/to the array.

#include <vector>
#include <string>
#include <algorithm>

std::string twoSort(std::vector<std::string> s)
{
    std::sort(s.begin(), s.end());
    std::string ans = s[0];
    std::string starred; 
    
    for (char& c : ans) {
        starred.push_back(c);
        starred.push_back('*');
        starred.push_back('*');
        starred.push_back('*');
    }
    starred.pop_back();
    starred.pop_back();
    starred.pop_back();
    return starred;
}