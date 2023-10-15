#![allow(warnings, unused)]
#[derive(Default)]
pub struct Car {
    fuel_eff: i32,
    size: i32,
}
impl Car {
    fn new(mut fe: i32, mut s: i32) -> Car {
        fuel_eff = fe;
        size = s;

        /*
            This is a constructor method.
            Please appropriate members to the struct constructor as per your logic.
            Currently the constructor returns a struct with all the defaults for the data types in the struct.
        */
        Car {
            ..Default::default()
        }
    }
}
impl Car {
    fn print(&mut self) {
        std::println!("Size: {}\nFuel efficiency: {}\n", self.size, self.fuel_eff);
    }
}
fn main() {}
