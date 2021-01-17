# 1351. Count Negative Numbers in a Sorted Matrix (Easy); 
# technically the array is sorted already so the naive approach works fine
def countNegatives(self, grid: List[List[int]]) -> int:
    negatives = 0
    for row in grid:
        for item in row:
            if item < 0:
                negatives += 1
    return negatives

# Time complexity: O(n^2)
# Space complexity: O(1)

# here's the binary search solution
def countNegatives(self, grid: List[List[int]]) -> int:
    negatives = 0
    m, n = len(grid), len(grid[0])
    row, col = 0, n - 1
    
    while row < m and col >= 0:
        if grid[row][col] < 0:
            negatives += m - row # take the last col
            col -= 1
        else:
            row += 1
        
    return negatives
# Time complexity: O(m + n)
# Space complexity: O(1)

# 1011. Capacity To Ship Packages Within D Days
def shipWithinDays(self, weights: List[int], D: int) -> int:
    lo = max(weights)
    hi = sum(weights)
    
    while (lo < hi):
        mid = (lo + hi) // 2
        days = 1
        curr = 0
        
        for weight in weights:
            if curr + weight > mid:
                days += 1
                curr = 0
            curr += weight
            
        if days > D:
            lo = mid + 1
        else:
            hi = mid

    return lo

# Time complexity: O(NlogN)
# Space complexity: O(1)

# 875. Koko Eating Bananas (Medium)
def minEatingSpeed(self, piles: List[int], H: int) -> int:    
    lo = 1
    hi = max(piles)
    while (lo < hi):
        mid = (lo + hi) // 2
        sumHours = 0
        for pile in piles:
            if pile - mid <= 0:
                sumHours += 1
            else:
                sumHours += ceil(pile / mid)
            # sumHours += (pile + mid - 1) // mid
        if sumHours > H:
            lo = mid + 1
        else:
            hi = mid
    return lo

# Time complexity: O(Nlog(MaxP))
# Space complexity: O(1)

# 852. Peak Index in a Mountain Array (Easy)
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    lo = 0
    hi = len(arr) - 1
    while (lo < hi):
        mid = (hi + lo) // 2
        if arr[mid] < arr[mid+1]:
            lo = mid + 1
        else:
            hi = mid
            
    return lo
# Time complexity: O(log(N))
# Space complexity: O(1)

# 744. Find Smallest Letter Greater Than Target (Easy)
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    left = 0
    right = len(letters) - 1
    
    while (left <= right):
        mid = left + (right - left) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return letters[left % len(letters)]
# Time complexity: O(log(n))
# Space complexity: O(1)

# 349. Intersection of Two Arrays (Easy)
# binary search solution
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    nums2.sort()
    for num in nums1:
        if self.binarySearch(nums2, num) and num not in res:
            res.append(num)
    return res

def binarySearch(self, arr, num):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = left + (right - left) // 2
        if arr[mid] == num:
            return True
        # num is smaller than the mid value
        # so we search on the left side
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

# Time complexity: O(nlog(n)) via the initial sort
# Space complexity: 0(1)

# one-liner (built-in set), very fast solution
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))

# Time complexity: O(n + m)
# Space complexity: O(n + m)

# 540. Single Element in a Sorted Array (Medium)
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) // 2
    while (lo < hi):
        mid = (lo + hi) // 2
        if nums[mid*2] == nums[mid*2+1]:
            lo = mid + 1
        else:
            hi = mid

    return nums[2*lo]

# Time complexity: O(logN)
# Space complexity: O(1)

# 392. Is Subsequence (Easy)

# Binary Search solution
def isSubsequence(self, s: str, t: str) -> bool:
    dp = dict()
    for idx, elem in enumerate(t):
        dp.setdefault(elem, []).append(idx)
        
    lastFound = -1
    for char in s:
        if not dp.get(char):
            return False
        j = self.binarySearch(dp[char], lastFound)
        if (j == -1):
            return False
        lastFound = j
        
    return True

def binarySearch(self, array, lastFound):
    lo = 0
    hi = len(array) - 1
    res = -1
    while (lo <= hi):
        mid = lo + (hi - lo) // 2
        if array[mid] > lastFound:
            res = array[mid]
            hi = mid - 1
        else:
            lo = mid + 1
            
    return res

# Time complexity: O(NlogN)
# Space complexity: O(N)

# 2 pointers solution
def isSubsequence(self, s: str, t: str) -> bool:
    pt1 = 0
    pt2 = 0
    
    while (pt1 < len(s) and pt2 < len(t)):
        if (s[pt1] == t[pt2]):
            pt1 += 1
        pt2 += 1
    
    return pt1 == len(s)

# Time complexity: O(N)
# Space complexity: O(1)


# 300. Longest Increasing Subsequence (Medium)
# optimal solution 1
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
def lengthOfLIS(self, nums: List[int]) -> int:
    tails = [0] * len(nums)
    size = 0
    for num in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1
            else:
                j = m
        tails[i] = num
        size = max(i + 1, size)
    return size

# Time complexity: O(Nlog(N))
# Space complexity: O(N)

# optimal solution 2
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [float('inf')] * n
    for i, num in enumerate(nums):
        update_pos = self.binarySearch(dp, num, i)
        dp[update_pos] = num
    
    res = [x for x in dp if x != float('inf')]
    return len(res)

def binarySearch(self, arr, target, hi):
    lo = 0
    while (lo <= hi):
        mid = lo + (hi - lo) // 2
        if target == arr[mid]: 
            return mid
        elif target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

# Time complexity: O(Nlog(N))
# Space complexity: O(N)

# O(n^2) solution
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 1
    res = 1
    for i in range(n):
        max_val = 0
        for j in range(i):
            if nums[i] > nums[j]:
                max_val = max(max_val, dp[j])
        dp[i] = max_val + 1
        res = max(res, dp[i])
    return res

# Time complexity: O(N^2)
# Space complexity: O(N)