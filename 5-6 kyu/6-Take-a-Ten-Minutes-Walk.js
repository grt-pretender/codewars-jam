/*
 You live in the city of Cartesia where all roads are laid out in a perfect grid. 
 You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
 The city provides its citizens with a Walk Generating App on their phones -- 
 everytime you press the button it sends you an array of one-letter strings 
 representing directions to walk (eg. ['n', 's', 'w', 'e']). 
 You always walk only a single block for each letter (direction) 
 and you know it takes you one minute to traverse one city block, 

 so create a function that will return true 
 if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
 and will, of course, return you to your starting point. 
 Return false otherwise.

 ==========================================================
*/

/*
 Note. Steps in different directions:
 'n' = [0, 1]  
 's' = [0, -1] 
 'w' = [-1, 0] 
 'e' = [1, 0] 
*/

/*
 ==========================
 1) One solution
 ==========================
*/
 
function isValidWalk(walk) {
	let walk_time = walk.length;
    let x_coordinate = 0;
    let y_coordinate = 0;

    if (walk_time !== 10)
    	return false;

    for (w of walk) {
    	switch (w) {
      case 'n': y_coordinate++; 
      	break
      case 's': y_coordinate--; 
      	break
      case 'w': x_coordinate--; 
      	break
      case 'e': x_coordinate++; 
      	break
    	}
    }
    return x_coordinate == 0 && y_coordinate == 0;
}


/*
 ==========================
 2) And another one
 ==========================
*/

function isValidWalk(walk) {
  let walk_time = walk.length;
  if (walk_time !== 10)
    return false;
  
  let dir = {
    n : 0,
    s : 0,
    w : 0,
    e : 0,
  }
  
  for (var i = 0; i < walk.length; i++) {
    dir[walk[i]]++;
  }
  
  if (dir["n"] == dir["s"] && dir["w"] == dir["e"])
    return true;
  else {
    return false;
  }
}
