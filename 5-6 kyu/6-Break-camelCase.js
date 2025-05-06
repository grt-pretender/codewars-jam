/* Complete the solution so that the function will break up camel casing, using a space between words:
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  "" */


/* 
=========================
1) Using regex
=========================
*/

function solution(string) {
  return string.split(/(?=[A-Z])/).join(' ');
}


/*
=========================
2) Using a new string
=========================
*/


function solution(string) {
  let ans = "";
  for (let c of string) {
    if (c == c.toUpperCase()) {
      ans += " ";
    }
    ans += c;
  }
  return ans;
}


/*
=========================
3) Using ternary operator
=========================
*/

function solution(string) {
  let ans = "";
  for (let c of string) {
    c == c.toUpperCase() ? (ans += " " + c) : (ans += c);
  }
  return ans;
}