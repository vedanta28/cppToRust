#include <iostream>

using namespace std;

enum HttpResponse : int {
  Okay = 200,
  NotFound = 404,
  InternalError = 500,
};

int main() {
  // cout << HttpResponse::InternalError;
}
