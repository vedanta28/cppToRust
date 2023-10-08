fn main() {
    let mut m_direction: i32 = 3;
    match m_Direction {
        1 => {
            println!("North");
        }
        2 => {
            println!("East");
        }
        3 => {
            println!("South");
        }
        4 => {
            println!("West");
        }
        _ => {
            println!("Invalid");
            return 0;
        }
    }
    return 1;
}
