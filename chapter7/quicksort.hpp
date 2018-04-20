#include <functional>
#include <type_traits>

template <typename RandomIt, typename Compare>
RandomIt q_partition(RandomIt first, RandomIt last, Compare cmp)
{
    auto lhs = first;
    auto rhs = lhs + 1;
    while (rhs != last) {
        if (cmp(*rhs, *first)) {
            ++lhs;
            std::iter_swap(lhs, rhs);
        }
        ++rhs;
    }
    std::iter_swap(first, lhs);
    return lhs;
}

template <typename RandomIt,
    typename Compare
    = std::less_equal<typename std::iterator_traits<RandomIt>::value_type>>
void quick_sort(RandomIt first, RandomIt last, Compare cmp = Compare())
{
    if (last - first >= 2) {
        RandomIt mid = q_partition(first, last, cmp);
        quick_sort(first, mid, cmp);
        quick_sort(mid + 1, last, cmp);
    }
}
