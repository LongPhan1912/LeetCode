# 1423. Maximum Points You Can Obtain from Cards (Medium)
def maxScore(self, cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    total = sum(cardPoints)
    if n == k:
        return total
    
    rem = n - k
    subArr = 0
    maxSum = 0
    for i in range(n):
        if i < rem:
            subArr += cardPoints[i]
        else:
            if i == rem:
                maxSum = total - subArr
            subArr += cardPoints[i] - cardPoints[i-rem]
            maxSum = max(maxSum, total - subArr)
    
    return maxSum

# A shorter solution
def maxScore(self, cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    m = n - k
    min_sum = s = sum(cardPoints[:m])
    for i in range(k):
        s = s - cardPoints[i] + cardPoints[m + i]
        min_sum = min(min_sum, s)
    return sum(cardPoints) - min_sum

# Time complexity: O(n)
# Space complexity: O(1)

# 1052. Grumpy Bookstore Owner (Medium)
def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    n = len(grumpy)
    max_gains = 0
    satisfied = 0
    for i in range(n):
        if grumpy[i] == 0:
            satisfied += customers[i]
        if i < X:
            max_gains += customers[i]*grumpy[i]
        else:
            if i == X:
                curr_sum = max_gains
            curr_sum += customers[i]*grumpy[i] - customers[i-X]*grumpy[i-X]
            max_gains = max(curr_sum, max_gains)
            
    return satisfied + max_gains

# Time complexity: O(n)
# Space complexity: O(1)

# 1004. Max Consecutive Ones III (Medium)
def longestOnes(self, A: List[int], K: int) -> int:
    start = 0
    for i in range(len(A)):
        K -= 1 - A[i]
        if K < 0:
            K += 1 - A[start]
            start += 1
            
    return i - start + 1

# Time complexity: O(n)
# Space complexity: O(1)

# 485. Max Consecutive Ones (Easy)
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res = 0
    curr = 0
    for n in nums:
        if n == 1:
            curr += 1
        else:
            res = max(curr, res)
            curr = 0
    
    return res if res > curr else curr

# Time complexity: O(n)
# Space complexity: O(1)