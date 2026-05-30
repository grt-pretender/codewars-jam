/*Jimmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each. 
If one of the flowers has an even number of petals 
and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower 
and return true if they are in love and false if they aren't.*/


bool check_even(int x) {
    bool is_even;
    if (x%2 == 0) {
      is_even = true;
    } else {
      is_even = false;
    }
    return is_even;
}

bool lovefunc(int f1, int f2) {
  return check_even(f1) == check_even(f2) ? false : true;
}