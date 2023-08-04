// Build a function that returns an array of integers from n to 1 where n>0.
// Example : n=5 --> [5,4,3,2,1]

// solution:

fn reverse_seq(n: u32) -> Vec<u32> {
    let upper_bound = n + 1;
    let mut _our_vec: Vec<u32> = (1..upper_bound).collect();
    _our_vec.sort_by_key(|a| std::u32::MAX - a);
    _our_vec
}

// or shorter version:

fn reverse_seq(n: u32) -> Vec<u32> {
    (1..n + 1).rev().collect()
}
