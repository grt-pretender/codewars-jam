/*
Write a function that takes an array of words 
 and smashes them together into a sentence and returns the sentence. 

 You can ignore any need to sanitize words or add punctuation, 
 but you should add spaces between each word. 

 Be careful, there shouldn't be a space at the beginning or the end of the sentence!
 */

/*
 ============================
 1) One solution
 ============================
 */

function smash (words) {
  return words.join(" ");
};


/*
 ============================
 2) And another one
 ============================
 */

function smash (words) {
  let ans = '';
  for(var i = 0; i<words.length; i++) {
    ans += words[i] + " ";
    }
  ans = ans.slice(0, -1); 
  return ans;
};


/*
 ============================
 3) Using diff types summation
 ============================
 */

function smash (words) {
   let ans = words + "";
   return ans.replace(/,/g," ");
};