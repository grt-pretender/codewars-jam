/*Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

Example #1: if we run 9119 through the function, 811181 will come out,
because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
*/

// 1) Long version)

fn square_digits(num: u64) -> u64 {
    let str_num: String = num.to_string();
    let numbers: Vec<u32> = str_num
        .chars()
        .map(|c| c.to_digit(10).expect("Not a valid digit"))
        .collect();

    let mut new_numbers: Vec<u32> = Vec::new();
    let mut new_string: String = String::new();

    for c in numbers.iter() {
        let new_c = c * c;
        new_numbers.push(new_c);
    }

    for el in new_numbers.iter() {
        let new_el = el.to_string();
        new_string += &new_el;
    }

    let ans: u64 = new_string.parse().unwrap();
    return ans;
}

// And a short fancy one

fn square_digits(num: u64) -> u64 {
    num.to_string()
        .chars()
        .map(|c| format!("{}", c.to_digit(10).unwrap().pow(2)))
        .collect::<String>()
        .parse()
        .unwrap()
}
