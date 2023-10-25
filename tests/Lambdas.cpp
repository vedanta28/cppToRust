int main() {
  auto num = 5;
  auto add_num_by_val = [=](int x) { return x + num; };
  auto add_num_by_ref = [&, num](int x) -> int { return x + num; };
}
