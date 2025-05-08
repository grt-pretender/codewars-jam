// Complete the solution so that it reverses the string passed into it.

fn solution(phrase: &str) -> String {
    let mut ans = phrase.chars().rev().collect::<String>();
    return ans;
}
