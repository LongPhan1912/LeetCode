// Just some random questions done in C++
// 1470. Shuffle the Array (Easy)
// memory-efficient method
vector<int> shuffle(vector<int>& nums, int n) {
    int j = 0;
    for (int i = 0; i < 2*n; i+=2) {
        int val = nums[n+(i/2)];
        nums.erase(nums.begin()+n+(i/2));
        nums.insert(nums.begin()+i+1, val);
    }
    return nums;
}
// Time complexity: O(N)
// Space complexity: O(1)

vector<int> shuffle(vector<int>& nums, int n) {
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        ans.push_back(nums[i]);
        ans.push_back(nums[i+n]);
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 1431. Kids With the Greatest Number of Candies (Easy)
vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    int greatest = 0;
    for (int i = 0; i < candies.size(); i++) {
        greatest = max(greatest, candies[i]);
    }
    vector<bool> ans;
    for (int i = 0; i < candies.size(); i++) {
        ans.push_back((candies[i]+extraCandies) >= greatest ? true : false);
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 66. Plus One (Easy)
vector<int> plusOne(vector<int>& digits) {
    int last = digits.size() - 1;
    bool carry = false;
    for (int i = last; i > -1; i--) {
        int val = digits[i];
        if (carry) {
            if (val == 9) { digits[i] = 0; }
            else { digits[i] += 1; carry = false; }
        } else {
            if (val == 9) { digits[i] = 0; carry = true; }
            else { digits[i] += 1; }
        }
        if (!carry) { break; }
    }
    if (carry) {
        digits.insert(digits.begin(), 1);
    }
    return digits;
}