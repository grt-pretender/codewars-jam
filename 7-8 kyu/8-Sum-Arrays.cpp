// Write a function that takes an array of numbers and returns the sum of the numbers. 
// The numbers can be negative. 
// If the array is empty, return 0.

#include <vector>
#include <numeric>

int sum(const std::vector<int> &nums) {

    if (nums.size() == 0) return 0;

    int sum = std::accumulate(nums.begin(), nums.end(), 0);
    return sum;
}