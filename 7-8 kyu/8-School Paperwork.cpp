/*
Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. 
If n < 0 or m < 0 return 0.
*/

/*
Basic solution
*/

int paperwork(int n, int m){
	int blank_pages_count;
	if (n < 0 || m < 0) return 0;
	blank_pages_count = n * m;
	return blank_pages_count;
}


/*
Basic solution, no extra variable 
*/

int paperwork(int n, int m){
  if(n<1||m<1)
    return 0;
  else return n*m;
}


/*
And short version 
*/

int paperwork(int n, int m) {
  return n < 0 || m < 0 ? 0 : n * m;
}