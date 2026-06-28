// In this simple assignment you are given a number and have to make it negative. 
// The number can be negative already, in which case no change is required.

package kata

func MakeNegative(x int) int {
  if (x > 0) {
    x *= -1
  }
  return x
}