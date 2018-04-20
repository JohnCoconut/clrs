#include <functional>
#include <iostream>
#include <array>
#include "quicksort.hpp"

int main()
{
  std::vector<int> v{ 3, 1, 4, 1, 5, 9, 2, 6 };
  std::array<int, 8> a;
  std::copy(v.begin(), v.end(), a.begin());
  quick_sort(v.begin(), v.end());
  quick_sort(a.begin(), a.end());
  for (auto i : a)
    std::cout << i << ' ';
  return 0;
}
