#![allow(warnings, unused)]
use std::*;
enum HttpResponse {
    Okay = 200,
    NotFound = 404,
    InternalError = 500,
}
fn main() {
    println!("{}", HttpResponse::InternalError);
}
