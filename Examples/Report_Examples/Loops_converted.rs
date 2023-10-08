fn main() {
    let mut n: i32 = 15;
    let mut a: i32 = 10;
    let mut b: i32 = 10;
    let mut c: i32 = 200;
    while a + b {
        b = b + 1;
    }
    let mut i: i32 = 2;
    while i <= n {
        c = a + b;
        a = b;
        b = c;
        i += 1;
    }
}
