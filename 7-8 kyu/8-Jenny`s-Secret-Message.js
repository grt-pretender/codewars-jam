/* Jenny has written a function that returns a greeting for a user. 
However, she's in love with Johnny, and would like to greet him slightly different. 
She added a special case to her function, but she made a mistake.
Can you help her?*/

/* 
==========================
1) Simple if-else
==========================
*/

function greet(name){
  if(name === "Johnny")
    return "Hello, my love!";
  else 
    return "Hello, " + name + "!";
}


/* 
==========================
2) Using ternary operator
==========================
*/

function greet(name){
  return "Hello, " + (name == "Johnny" ? "my love" : name) + "!";
}



/* 
==========================
3) Using switch
==========================
*/

function greet(name){
  switch (name) {
    case "Johnny":
      return "Hello, my love!";
      break;
    default: 
      return "Hello, " + name + "!";
      }
}
