int main() {
  int y = 2;
  auto mul_by_val = [=](int x) { return x * y; };
  auto mul_by_ref = [&, y](int x) -> int { return x * y; };
}
