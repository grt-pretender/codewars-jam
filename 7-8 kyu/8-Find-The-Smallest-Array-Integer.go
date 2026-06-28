// Given an array of integers your solution should find the smallest integer.
// You can assume, for the purpose of this kata, that the supplied array will not be empty.

package kata

import (
	"sort"
)

// 1) Short solution

func SmallestIntegerFinder(numbers []int) int {
  sort.Ints(numbers)
  return numbers[0]
}

// 2) Sorting the array manually 

package kata

func SmallestIntegerFinder(numbers []int) int {
	smallestNum := numbers[0]
	for i := range numbers {
		if numbers[i] < smallestNum {
			smallestNum = numbers[i]
		}
	}
	return smallestNum
}