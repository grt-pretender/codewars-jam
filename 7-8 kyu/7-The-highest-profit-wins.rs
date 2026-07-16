/* Ben has a very simple idea to make some profit: he buys something and sells it again.
Of course, this wouldn't give him any profit at all if he was simply to buy and sell it
at the same price. Instead, he's going to buy it for the lowest possible price
and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

Examples
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]
        --> [1,1]
Remarks
All arrays or lists will always have at least one element, so you don't need to check the length.
Also, your function will always get an array or a list, you don't have to check for null,
undefined or similar.*/

// 1) One solution - from vec to tuple

fn min_max(lst: &[i32]) -> (i32, i32) {
    let mut output = Vec::new();
    if let Some(&min_val) = lst.iter().min() {
        output.push(min_val);
    }
    if let Some(&max_val) = lst.iter().max() {
        output.push(max_val);
    }

    let tuple = (output[0], output[1]);
    return tuple;
}

// 2) And a short one

fn min_max(lst: &[i32]) -> (i32, i32) {
    (*lst.iter().min().unwrap(), *lst.iter().max().unwrap())
}
