/*
 Trolls are attacking your comment section!

 A common way to deal with this situation is to remove all of the vowels 
 from the trolls' comments, neutralizing the threat.

 Your task is to write a function that takes a string 
 and return a new string with all vowels removed.

 For ex, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
 Note: for this kata y isn't considered a vowel.
*/


/*
===================================
1) Using regex
===================================
*/

function disemvowel(str) {
  return str.replace(/[aeiou]/gi, '');
}


/*
===================================
2) Using a new string
===================================
*/


function disemvowel(str) {
    let ans = "";
    let pattern = "aeiou";

    for (let c of str) {
        if (pattern.includes(c.toLowerCase())) 
        	continue;
        ans += c;
    }
    return ans;
}