// Complete the solution so that it reverses the string passed into it.


/* 
===================================
1) One solution
===================================
*/

function solution(str){
    return str.split("").reverse().join("");
}



/* 
===================================
2) Using decrement loop
===================================
*/

function solution(str) {
    let ans = "";
    for (let i = str.length - 1; i >= 0; i--) {
        ans += str[i];
    }
    return ans;
}


