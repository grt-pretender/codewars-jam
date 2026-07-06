// Given a month as an integer from 1 to 12, return to which quarter of the year 
// it belongs as an integer number.

package kata

func Maps(x []int) []int {
    result := make([]int, len(x))
    
    for i, val := range x {
        result[i] = val * 2
    }
    
    return result
}