use std::io;

fn main() {
    println!("Please enter your name :");
    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");

    println!("Please enter your age :");
    let mut age = String::new();
    io::stdin()
        .read_line(&mut age)
        .expect("Failed to read line");

    println!("Please enter your gender :");
    let mut gender = String::new();
    io::stdin()
        .read_line(&mut gender)
        .expect("Failed to read line");        

    // convert age from String to i32     
    let age: i32 = age.trim().parse().expect("Please type a number! as age");

    // .trim() is used to remove the newline character from the input (auto assigned)
    println!("Your Name: {}, Age: {}, Gender: {}", name.trim(), age, gender.trim());
}
