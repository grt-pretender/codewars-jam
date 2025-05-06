/* Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different.
She added a special case to her function, but she made a mistake.
Can you help her?*/

/*
==========================
1) Simple if-else
==========================
*/

fn greet(input: &str) -> String {
    if input == "Johnny" {
        return "Hello, my love!".to_string();
    };
    format!("Hello, {}!", input)
}

/*
==========================
2) Using ternary operator
==========================
*/

fn greet(input: &str) -> String {
    let mut check_name = if input == "Johnny" { "my love" } else { input };
    format!("Hello, {}!", check_name)
}

/*
==========================
3) Using match
==========================
*/

fn greet(input: &str) -> String {
    match input {
        "Johnny" => "Hello, my love!".to_string(),
        _ => format!("Hello, {}!", input),
    }
}
