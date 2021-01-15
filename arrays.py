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
