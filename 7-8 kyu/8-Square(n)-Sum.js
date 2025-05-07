/*
Complete the square sum function so that 
it squares each number passed into it and then sums the results together.
*/


/*
===================================
1) One solution
===================================
*/

function squareSum(numbers) {
  let sum = 0;
  for( let i = 0; i < numbers.length; i++) {
      sum += Math.pow(numbers[i], 2);
  }
  return sum;
}


/*
===================================
2) With map/reduce
===================================
*/

function squareSum(numbers) {
  return numbers.map(n => n ** 2).reduce((a, b) => a + b, 0);
}


