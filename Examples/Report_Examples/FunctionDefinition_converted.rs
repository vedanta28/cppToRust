fn do_nothing(mut k: i32) {
    k = k + 1;
    k += 1;
    println!("This function does nothing\n");
}
fn fib(mut n: i32) -> i32 {
    let mut a: i32 = 0;
    let mut b: i32 = 1;
    let mut c: i32;
    if n == 0 {
        return a;
    }
    let mut i: i32 = 2;
    while i <= n {
        c = a + b;
        a = b;
        b = c;
        i += 1;
    }
    return b;
}
fn random_function(mut a: char, mut b: char, mut status: bool) -> char {
    return if status { a } else { b };
}
fn main() {
    let mut n: i32 = 11;
    let mut a: i32 = fib(n);
    let mut flag: bool = false;
    let mut input1: char = 'm';
    let mut output: char = random_function('l', input1, flag);
    do_nothing(555);
    println!("{}\n", output);
    println!("Fibonacci {}\n", fib(n));
}
