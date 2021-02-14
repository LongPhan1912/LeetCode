# 1752. Check if Array Is Sorted and Rotated (Easy)
def check(self, nums: List[int]) -> bool:
    sortedArr = sorted(nums)
    n = len(nums)
    rotate = 0
    for idx in range(1, n):
        if nums[idx] < nums[idx-1]:
            rotate = idx
            break

    rotatedArr = [-1]*n
    for idx in range(n):
        rotatedArr[idx] = nums[(idx+rotate)%n]

    return rotatedArr == sortedArr

# Time complexity: O(NlogN)
# Space complexity: 0(N)

# 1608. Special Array With X Elements Greater Than or Equal X (Easy)
def specialArray(self, nums: List[int]) -> int:
    # sort the array in order
    nums.sort() 
    # if the number of elements is less than the value of the first element, return the array length
    # example: return 2 for array [3, 5]
    # i.e. there are 2 elements greater than or equal to 2
    if len(nums) <= nums[0]: 
        return len(nums)
    for i in range(1, len(nums)): 
        remaining_elems = len(nums) - i
        if nums[i-1] < remaining_elems <= nums[i]: 
            return remaining_elems
    return -1
    
# Time complexity: O(n)
# Space complexity: 0(1)


# 1588. Sum of All Odd Length Subarrays (Easy)
# explanation: https://www.youtube.com/watch?v=J5IIH35EBVE 
def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    sum = 0
    n = len(arr)
    for i in range(n):
        # subarrays that start with arr[i]: (n - i)
        # subarrays that end with arr[i]: (i + 1)
        # and since we are only looking at odd length arrays, 
        # we add one to the product and divide the whole thing by 2
        sum += arr[i] * (((i + 1) * (n - i) + 1) // 2)
    return sum

# Time complexity: O(n)
# Space complexity: 0(1)

# 1572. Matrix Diagonal Sum (Easy)
def diagonalSum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    mid = n // 2
    sum = 0
    if n % 2 != 0:
        sum -= mat[mid][mid]
    
    for i in range(n):
        sum += mat[i][i] + mat[n - i - 1][i]
    return sum

# Time complexity: O(n)
# Space complexity: 0(1)

# 1437. Check If All 1's Are at Least Length K Places Away (Medium, but actually Easy)
# two pointers
def kLengthApart(self, nums: List[int], k: int) -> bool:
    left = -1
    right = -1
    for i in range(len(nums)):
        if nums[i] == 1:
            if left == -1:
                left = i
                continue
            if left != -1 and right == -1:
                right = i
                if right - left - 1 < k:
                    return False
                else:
                    left = i
                    right = -1
    return True

# count the zeroes
def kLengthApart(self, nums: List[int], k: int) -> bool:
    count = k
    for num in nums:
        if num == 1:
            if count < k:
                return False
            count = 0
        else:
            count += 1
            
    return True

# Time complexity: O(n)
# Space complexity: 0(1)

# 1395. Count Number of Teams (Medium)
def numTeams(self, rating: List[int]) -> int:
    res = 0
    n = len(rating)
    greater = dict()
    lesser = dict()
    for i in range(n-1):
        for j in range(i+1, n):
            if rating[i] < rating[j]:
                # count how many numbers after rating[i] are greater than it
                greater[i] = greater.get(i, 0) + 1
            else:
                # count how many numbers after rating[i] are less than it
                lesser[i] = lesser.get(i, 0) + 1
    
    for i in range(n-2):
        for j in range(i+1, n):
            if rating[i] < rating[j]:
                # add how many numbers are greater than rating[i] and rating[j]
                res += greater.get(j, 0)
            else:
                # add how many numbers are less than rating[j] and rating[i]
                res += lesser.get(j, 0)
    return res

# Time complexity: O(n^2)
# Space complexity: 0(n)

# 1338. Reduce Array Size to The Half (Medium)
# sorting dictionary keys solution
def minSetSize(self, arr: List[int]) -> int:
    freq = dict()
    half = ceil(len(arr) / 2)
    for elem in arr:
        freq[elem] = freq.get(elem, 0) + 1
        if freq[elem] >= half:
            return 1
    keys_ascending_order = sorted(freq, key=lambda x:freq[x], reverse=True)
    sum = 0
    count = 0
    for i, key in enumerate(keys_ascending_order):
        count += freq[key]
        if count >= half:
            break
    return i + 1

# Time complexity: O(nlog(n))
# Space complexity: 0(n)

# heap solution
def minSetSize(self, arr: List[int]) -> int:
    freq = dict()
    half = ceil(len(arr) / 2)
    for elem in arr:
        freq[elem] = freq.get(elem, 0) + 1
        
    x = list(freq.values())
    x= [-i for i in x]
    heapq.heapify(x)
    sum = 0
    i = 0
    while sum < half:
        var = -heapq.heappop(x)
        sum += var
        i+=1
    return i

# Time complexity: O(n) // build heap / heapify and loops are O(n)
# Space complexity: 0(n)

# 771. Jewels and Stones (Easy)
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    stoneTable = {}
    for stone in stones:
        stoneTable[stone] = stoneTable.get(stone, 0) + 1

    ans = 0
    for jewel in jewels:
        if stoneTable.get(jewel):
            ans += stoneTable[jewel]

    return ans

# Sol 2:
# 	stoneSet = set(jewels)
#         ans = 0
#         for stone in stones:
#             if stone in stoneSet:
#                 ans += 1
                
#     return ans

# Time complexity: O(n)
# Space complexity: 0(n)


# 442. Find All Duplicates in an Array (Medium)
# fast solution
def findDuplicates(self, nums: List[int]) -> List[int]:
    appearance = dict()
    ans = []
    for elem in nums:
        appearance[elem] = appearance.get(elem, 0) + 1
        if appearance[elem] == 2:
            ans.append(elem)
    return ans

# Time complexity: O(n)
# Space complexity: 0(n)

# more memory efficient solution
def findDuplicates(self, nums: List[int]) -> List[int]:
    ans = []
    for elem in nums:
        if nums[abs(elem) - 1] >= 0:
            nums[abs(elem) - 1] *= -1
        else:
            # a negative number means we have seen it before
            ans.append(abs(elem))
    return ans

# Time complexity: O(n)
# Space complexity: 0(1)

# 350. Intersection of Two Arrays II (Easy)
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    
    ptr1, ptr2 = 0, 0
    result = []
    while (ptr1 < len(nums1) and ptr2 < len(nums2)):
        curr1, curr2 = nums1[ptr1], nums2[ptr2]
        if curr1 == curr2:
            result.append(curr1)
            ptr1 += 1
            ptr2 += 1
        elif curr1 < curr2:
            ptr1 += 1
        else:
            ptr2 += 1
    
    return result

# Time complexity: O(NlogN)
# Space complexity: 0(1)

# 283. Move Zeroes (Easy)
# memory-efficient solution
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    z = 0
    for idx, num in enumerate(nums):
        if (num != 0):
            nums[z], nums[idx] = nums[idx], nums[z]
            z += 1
        
    return nums

# Time complexity: O(N)
# Space complexity: 0(1)

# Queue data structure
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    queue = []
    countZeroes = 0
    for num in nums:
        if (num != 0):
            queue.append(num)
        else:
            countZeroes += 1
    
    queue += [0] * countZeroes
    for i in range(len(nums)):
        nums[i] = queue[i]
        
    return nums

# Time complexity: O(N)
# Space complexity: 0(N)

# 268. Missing Number (Easy)
def missingNumber(self, nums: List[int]) -> int:
    if len(nums) == 0: 
        return 0
    
    arr_total = sum(nums)
    total_with_missing_num = 0
    for i in range(len(nums)+1):
        total_with_missing_num += i
    
    return total_with_missing_num - arr_total

# Time complexity: O(N)
# Space complexity: 0(1)

# 242. Valid Anagram (Easy)
from collections import Counter
def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Time complexity: O(n)
# Space complexity: 0(1)

# 217. Contains Duplicate (Easy)
def containsDuplicate(self, nums: List[int]) -> bool:
    dp = dict()
    for num in nums:
        dp[num] = dp.get(num, 0) + 1
        if dp[num] >= 2: return True
    return False

# Time complexity: O(n)
# Space complexity: 0(n)

# 198. House Robber (Medium)
# Really great explanation: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
def rob(self, nums: List[int]) -> int:
    if len(nums) == 0: return 0
    elif len(nums) <= 2: return max(nums)
    prefix = [0, nums[0]]
    for i in range(1, len(nums)):
        curr = nums[i]
        prefix.append(max(prefix[i], prefix[i-1]+curr))
        print(prefix)
    
    return prefix[-1]

# Time complexity: O(n)
# Space complexity: 0(n)

# 136. Single Number (Easy)
def singleNumber(self, nums: List[int]) -> int:
    if (len(nums) == 1): 
        return nums[0]
    s = {}
    for num in nums:
        s[num] = s.get(num, 0) + 1
    
    for num in s:
        if s[num] == 1: return num
    return -1

# Time complexity: O(n)
# Space complexity: 0(n)

# Bit Manipulation
def singleNumber(self, nums):
    a = 0
    for i in nums:
        a ^= i
    return a
# Time complexity: O(n)
# Space complexity: 0(1)

# 128. Longest Consecutive Subsequence (Hard)
# Sorting solution
def longestConsecutive(self, nums: List[int]) -> int:
    currCount = 1
    maxCount = 0
    if len(nums) <= 1:
        return len(nums)
    
    nums.sort()
    prevNum = nums[0]
    for i in range(1, len(nums)):
        currNum = nums[i]
        if currNum == prevNum:
            continue
        elif currNum - prevNum == 1:
            currCount += 1
            maxCount = max(maxCount, currCount)
        else:
            currCount = 1
        prevNum = currNum
    return maxCount

# Time complexity: O(NlogN)
# Space complexity: 0(1)

# Hash set solution
def longestConsecutive(self, nums: List[int]) -> int:
    maxCount = 0
    hashSet = set(nums)
    
    for num in hashSet:
        currNum = num
        currCount = 1
        
        while currNum + 1 in hashSet:
            currCount += 1
            currNum += 1
        
        maxCount = max(maxCount, currCount)
    
    return maxCount

# Time complexity: O(N)
# Space complexity: 0(N)

# 121. Best Time to Buy and Sell Stock (Easy)
def maxProfit(self, prices: List[int]) -> int:
    mini = float('inf')
    profit = 0
    for price in prices:
        if mini > price: 
            mini = price
        elif profit < price - mini:
            profit = price - mini
    
    return profit
# Time complexity: O(n)
# Space complexity: 0(1)

# 56. Merge Intervals (Medium)
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = [intervals[0]]
    
    for idx in range(1, len(intervals)):
        curr = intervals[idx]
        back = res[-1]
        if back[1] >= curr[0]:
            res.pop()
            res.append([back[0], max(curr[1], back[1])])
        else:
            res.append(curr)
            
    return res
# Time complexity: O(NlogN)
# Space complexity: 0(N)

# 53. Maximum Subarray (Easy)
# sliding window technique
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum <= num: # skip the previous subarray
            curr_sum = num
        max_sum = max(max_sum, curr_sum)
    return max_sum

# similar dynamic programming approach
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0: # reset curr_sum
            curr_sum = 0
    return max_sum

# Time complexity: O(n)
# Space complexity: 0(1)

# 48. Rotate Image (Medium)
# Rotate 4 cells approach
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for row in range(n//2):
        for col in range(row, n-1-row):
            matrix[row][col], matrix[col][n-1-row] = matrix[col][n-1-row], matrix[row][col]
            matrix[row][col], matrix[n-1-row][n-1-col] = matrix[n-1-row][n-1-col], matrix[row][col]
            matrix[row][col], matrix[n-1-col][row] = matrix[n-1-col][row], matrix[row][col]

# Time complexity: O(M) where M is the number of cells in the matrix
# Space complexity: 0(1)

# Transpose then reflect method
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    self.transpose(matrix)
    self.reflect(matrix)

def transpose(self, matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
def reflect(self, matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# Time complexity: O(M) where M is the number of cells in the matrix
# Space complexity: 0(1)

# 1. Two Sum (Easy)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    complementary = dict()
    for i, v in enumerate(nums):
        complement = target - v 
        if complement in complementary:
            return [complementary[complement], i]
        else:
            complementary[v] = i
    return [-1, -1]

# Time complexity: O(n)
# Space complexity: 0(n)
