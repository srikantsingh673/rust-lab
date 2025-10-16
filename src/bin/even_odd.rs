use std::io;

fn main() {
    println!("Please enter a Number :");
    let mut number = String::new();
    
    io::stdin()
        .read_line(&mut number)
        .expect("Failed to readline");
    
    let number: i32 = number.trim().parse().expect("Please type Number only :");

    if (number%2) == 0 {
        println!("Entered number {} is Even", number)
    }
    else {
        println!("Entered number {} is Odd", number)
    }
}