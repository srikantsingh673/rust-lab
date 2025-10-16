use std::io;

fn main() {
    println!("Please enter your Choice [1 or 2] :");
    println!("1. C to F \n2. F to C");

    let mut choice = String::new();
    
    io::stdin()
        .read_line(&mut choice)
        .expect("Failed to readline");
    
    if choice.trim() == "1"
    {
        c_to_f();
    }
    else if choice.trim() == "2"
    {
        f_to_c();
    }
    else {
        println!("Please enter valid choice");
    }

}

// Function to convert Celsius to Fahrenheit
fn c_to_f() {
    println!("Please enter temperature in Celsius :");
    let mut c = String::new();

    io::stdin()
        .read_line(&mut c)
        .expect("Failed to readline");

    let c: f32 = c.trim().parse().expect("Please type Number only :");
    let result : f32 = (c * 1.8) + 32.0;

    println!("{} Celsius into Fahrenheit {}", c, result);

}

// Function to convert Fahrenheit to Celsius
fn f_to_c() {
    println!("Please enter temperature in Fahrenheit :");
    let mut f = String::new();

    io::stdin()
        .read_line(&mut f)
        .expect("Failed to readline");

    let f: f32 = f.trim().parse().expect("Please type Number only :");
    let result : f32 = (f - 32.0) / 1.8;

    println!("{} Fahrenheit into Celsius {}", f, result);

}
