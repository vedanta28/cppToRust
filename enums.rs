#[derive(Debug)]
enum HttpResponse {
    Okay = 200,
    NotFound = 404,
    InternalError = 500,
}

#[derive(Debug)]
enum Gender { Male, Female }

fn main() {
    println!("{:?}", HttpResponse::InternalError);
    let g = Gender::Male;
    println!("{:?}", g);
}
