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

# 221. Maximal Square (Medium)
def maximalSquare(self, matrix: List[List[str]]) -> int:
    r = len(matrix)
    c = 0 if r <= 0 else len(matrix[0])

    dp = [[0]*(c+1) for i in range(r+1)]
    ans = 0
    for i in range(1, r+1):
        for j in range(1, c+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])

    return ans**2
# Time complexity: O(N^2)
# Space complexity: 0(N^2)

# 139. Word Break (Medium)
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True

    # is there a word lying between j and i that matches a word in the wordDict?
    # dp[j] means that you can start from point j onwards so to make a word
    # when you get a valid word from j to i, 
    # then dp[i], which later becomes dp[j], can give you a new starting point
    # and the process continues
    for i in range(1, n+1):
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]
# Time complexity: O(N^2)
# Space complexity: 0(N)

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

# 64. Minimum Path Sum (Medium)
def minPathSum(self, grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    for col in range(1, m):
        grid[0][col] += grid[0][col-1]

    for row in range(1, n):
        grid[row][0] += grid[row-1][0]


    for row in range(1, n):
        for col in range(1, m):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])

    return grid[n-1][m-1]
# Time complexity: O(N^2)
# Space complexity: O(1) as we are remodifying the given array

# 62. Unique Paths (Medium)
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0]*n for i in range(m)]
    for row in range(m):
        dp[row][0] = 1
    for col in range(n):
        dp[0][col] = 1

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[m-1][n-1]
# Time complexity: O(N^2)
# Space complexity: O(N^2)

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

# 38. Count and Say (Easy, but should be Medium)
def countAndSay(self, n: int) -> str:
    dp = [""]*(n)
    dp[0] = "1"

    count = 1
    prev = None
    val = ""

    idx = 1
    while (idx < n):
        string = dp[idx-1]
        for curr in string:
            if prev is None:
                prev = curr
                continue
            if prev != curr:
                val += str(count) + prev
                prev = curr
                count = 1
            elif prev == curr:
                count += 1

        val += str(count) + prev
        dp[idx] = val
        prev = None
        count = 1
        val = ""
        idx += 1

    return dp[n-1]

# Time complexity: O(S*N) where S is the length of the string stored in the DP table at (idx-1) and N is the number given
# Space complexity: O(M) where M is the size of the DP table
