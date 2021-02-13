# 1664. Ways to Make a Fair Array (Medium)
def waysToMakeFair(self, nums: List[int]) -> int:
    count = 0
    right = [0,0]
    left = [0, 0]

    for idx, num in enumerate(nums):
        right[idx % 2] += num

    for idx, num in enumerate(nums):
        right[idx % 2] -= num
        if (left[0] + right[1] == left[1] + right[0]):
            count += 1
        left[idx % 2] += num
    return count
# Time complexity: O(N)
# Space complexity: O(1)

# 1314. Matrix Block Sum (Medium)
def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    prefix = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]

    # Explanation for prefix sum: https://www.youtube.com/watch?v=PwDqpOMwg6U

    res = [[0] * (n) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            up = max(0, i - K)
            left = max(0, j - K)
            down = min(m, i + K + 1)
            right = min(n, j + K + 1)
            res[i][j] = prefix[down][right] - prefix[up][right] - \
                        prefix[down][left] + prefix[up][left]

    # Explanation for res table: https://leetcode.com/problems/matrix-block-sum/discuss/477036/JavaPython-3-PrefixRange-sum-w-analysis-similar-to-LC-30478
    return res

# Time complexity: O(m * n)
# Space complexity: O(m * n)

# 1025. Divisor Game (Easy)
def divisorGame(self, N: int) -> bool:
    return N % 2 == 0

# Time complexity: O(1)
# Space complexity: O(1)

# 746. Min Cost Climbing Stairs (Easy)
def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i-1], cost[i-2])

    return min(cost[n - 1], cost[n - 2])

# Time complexity: O(n)
# Space complexity: O(1)

# 392. Is Subsequence (Easy)
# two pointers
def isSubsequence(self, s: str, t: str) -> bool:
    pt1 = 0
    pt2 = 0

    while (pt1 < len(s) and pt2 < len(t)):
        if (s[pt1] == t[pt2]):
            pt1 += 1
        pt2 += 1

    return pt1 == len(s)

# Time complexity: O(n)
# Space complexity: O(1)

# 322. Coin Change (Medium)
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for num in range(1, amount+1):
        for denom in coins:
            if denom <= num:
                dp[num] = min(dp[num], dp[num-denom]+1)

    return dp[amount] if dp[amount] <= amount else -1
# Time complexity: O(S*N) where S is the size of the DP table and N is the total number of elems
# Space complexity: O(S)

# 121. Best Time to Buy and Sell Stock (Easy) -- technically not DP, but is categorised as such lol
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

# 70. Climbing Stairs (Easy)
def climbStairs(self, n: int) -> int:
    dp = {}
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

# Time complexity: O(n)
# Space complexity: O(n)

# fibonacci formula
def climbStairs(self, n: int) -> int:
    sqrtFive = sqrt(5)
    fib = ((1 + sqrtFive) / 2)**(n+1) - ((1 - sqrtFive) / 2)**(n+1)
    return int(fib // sqrtFive)

# Time complexity: O(logN)
# Space complexity: O(1)

# 53. Maximum Subarray (Easy)
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
# Space complexity: O(1)
