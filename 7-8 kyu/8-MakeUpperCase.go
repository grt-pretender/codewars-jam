// Write a function which converts the input string to uppercase.

#include <string>
#include <algorithm> 

std::string makeUpperCase(const std::string& str) {
  std::string newString = str;
  transform(newString.begin(), newString.end(), newString.begin(), ::toupper);
  return newString;
}