// Given a month as an integer from 1 to 12, return to which quarter of the year 
// it belongs as an integer number.

// 1) Solution with switch

int quarter_of(int month){
    int whichQuarter = 0;
    
    switch (month) {
    case 1:
    case 2:
    case 3:
        whichQuarter = 1;
        break;
    case 4:
    case 5:
    case 6:
        whichQuarter = 2;
        break;
    case 7:
    case 8:
    case 9:
        whichQuarter = 3;
        break;
    case 10:
    case 11:
    case 12:
        whichQuarter = 4;
        break;
      }
    return whichQuarter;
  }


// 2) Short solution 

int quarter_of(int month)
{
  return month <= 3 ? 1 : month <= 6 ? 2 : month <= 9 ? 3 : 4;
}