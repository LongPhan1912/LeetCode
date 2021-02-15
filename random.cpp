// Just some random questions done in C++

// 1725. Number Of Rectangles That Can Form The Largest Square (Easy)
int countGoodRectangles(vector<vector<int>>& rectangles) {
    int max = -1;
    int ans = 0;
    for (auto& row : rectangles) {
        int side = min(row[0], row[1]);
        if (max < side) {
            ans = 1;
            max = side;
        } else if (max == side) {
            ans++;
        }
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(1)

// 1672. Richest Customer Wealth (Easy)
int maximumWealth(vector<vector<int>>& accounts) {
    int res = 0;
    for (auto& it: accounts) {
        int sum = 0;
        for (int num : it) {
            sum += num;
        }
        res = max(sum, res);
    }
    return res;
}
// Time complexity: O(N^2)
// Space complexity: O(1)

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

// 1342. Number of Steps to Reduce a Number to Zero (Easy)
int numberOfSteps (int num) {
    int steps = 0;
    while (num != 0) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num -= 1;
        }
        steps += 1;
    }
    return steps;
}
// Time complexity: O(N)
// Space complexity: O(1)

// 1299. Replace Elements with Greatest Element on Right Side (Easy)
vector<int> replaceElements(vector<int>& arr) {
    int m = INT_MIN;
    for (int i = arr.size()-1; i > -1; i--) {
        if (m == INT_MIN) { m = arr[i]; }
        if (i == arr.size()-1) {
            arr[i] = -1;
        } else {
            int temp = max(m, arr[i]);
            arr[i] = m;
            m = temp;
        }
    }
    return arr;
}
// Time complexity: O(N)
// Space complexity: O(1)

// 118. Pascal's Triangle (Easy)
vector<vector<int>> generate(int numRows) {
    vector<vector<int>> ans;
    if (numRows == 0) {
        return ans;
    }

    vector<int> curr;
    curr.push_back(1);
    ans.push_back(curr);
    curr.clear();

    for (int i = 1; i < numRows; i++) {
        curr.push_back(1);
        for (int j = 1; j < i; j++) {
            curr.push_back(ans[i-1][j-1] + ans[i-1][j]);
        }
        curr.push_back(1);
        ans.push_back(curr);
        curr.clear();
    }
    return ans;
}
// Time complexity: O(N^2)
// Space complexity: O(N^2)

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
// Time complexity: O(N)
// Space complexity: O(1)

// 33. Search in Rotated Sorted Array (Medium)
int search(vector<int>& nums, int target) {
    int n = nums.size();
    if (n == 1) {
        if (nums[0] == target) { return 0; }
        else { return -1; }
    }
    // Linear scan
    // for (int i = 0; i < n; i++) {
    //     if (nums[i] == target) {
    //         return i;
    //     }
    // }
    // return -1;
    int lo = 0;
    int hi = n-1;
    
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] >= nums[lo]) {
            if (nums[lo] <= target && nums[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        } else {
            if (nums[hi] >= target && nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }
    return nums[lo] == target ? lo : -1;
}

// Accounting for rotation:
int search(vector<int>& nums, int target) {
    int n = nums.size();
    int lo = 0;
    int hi = n-1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (nums[mid] > nums[hi]) { lo = mid + 1; }
        else { hi = mid; }
    }
    int rotation = lo;
    lo = 0;
    hi = n-1;
    
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int trueMid = (mid+rotation) % n;
        if (nums[trueMid] == target) {
            return trueMid;
        } else if (nums[trueMid] > target) {
            hi = mid-1;
        } else {
            lo = mid+1;
        }
    }
    return -1;
}
// Time complexity: O(logN)
// Space complexity: O(1)

// 16. 3Sum Closest (Medium)
int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        sum += nums[i];
    }
    for (int i = 0; i < nums.size()-2; i++) {
        int lo = i+1;
        int hi = nums.size() - 1;
        while (lo < hi) {
            int currSum = nums[i] + nums[lo] + nums[hi];
            if (abs(currSum - target) < abs(sum - target)) {
                sum = currSum;
            }
            if (currSum == target) return currSum;
            else if (currSum < target) lo += 1;
            else hi -= 1;
        }
    }
    return sum;
}

// 8. String to Integer (atoi) (Medium)
int myAtoi(string s) {
    if (s.length() == 0 || isalpha(s[0])) return 0;
    int i = 0;
    while (i < s.length() && s[i] == ' ') {i++;}
    int sign = 1;
    if (s[i] == '-' || s[i] == '+') {
        sign = (s[i++] == '+') ? : -1;
    }
    int res = 0;
    int base = INT_MAX / 10;
    while (isdigit(s[i])) {
        if (res > base || (res == base && s[i] - '0' > 7)) 
            return (sign != 0 && sign > 0) ? INT_MAX : INT_MIN;
        res = 10 * res + (s[i++] - '0');
    }
    return sign * res;
}
// Time complexity: O(N)
// Space complexity: O(1)
