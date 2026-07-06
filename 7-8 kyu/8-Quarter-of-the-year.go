// Given a month as an integer from 1 to 12, return to which quarter of the year 
// it belongs as an integer number.

package kata

func QuarterOf(month int) int {
    
    whichQuarter := 0

    switch month {
    case 1, 2, 3:
        whichQuarter = 1
    case 4, 5, 6:
        whichQuarter = 2
    case 7, 8, 9:
        whichQuarter = 3
    case 10, 11, 12:
        whichQuarter = 4
      }
    return whichQuarter
  }

