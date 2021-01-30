# 1512. Number of Good Pairs (Easy)
def numIdenticalPairs(self, nums: List[int]) -> int:
    pairs = {}
    for num in nums:
        pairs[num] = pairs.get(num, 0) + 1

    ans = 0
    for num, count in pairs.items():
        ans += (count - 1) * count // 2

    return ans

# Time complexity: O(N)
# Space complexity: O(N)

# 1365. How Many Numbers Are Smaller Than the Current Number (Easy)
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    ans = []
    d = {}

    for idx, num in enumerate(sorted(nums)):
        if num not in d:
            d[num] = idx

    for num in nums:
        ans.append(d[num])
    return ans

# Time complexity: O(NlogN)
# Space complexity: O(N)

# 1160. Find Words That Can Be Formed by Characters (Easy)

# Extremely slow solution
def countCharacters(self, words: List[str], chars: str) -> int:
    sortedCharArr = sorted(chars)
    ans = 0
    for word in words:
        ans += self.findWordInChars(word, sortedCharArr)
    return ans

def findWordInChars(self, word, sortedCharArr):
    sortedWordArr = sorted(word)
    count = 0
    ptr1, ptr2 = 0, 0
    n, m = len(sortedWordArr), len(sortedCharArr)
    while (ptr1 < n and ptr2 < m):
        w = sortedWordArr[ptr1]
        c = sortedCharArr[ptr2]
        if w == c:
            ptr1 += 1
            ptr2 += 1
            count += 1
        elif w < c:
            ptr1 += 1
        else:
            ptr2 += 1
    return n if count == n else 0

# Faster solution
def countCharacters(self, words: List[str], chars: str) -> int:
    ans = 0
    for word in words:
        allPresent = True
        for char in word:
            if char not in chars or word.count(char) > chars.count(char):
                allPresent = False
                break
        if allPresent:
            ans += len(word)

    return ans

# Time complexity: O(N^2)
# Space complexity: O(1)

# 974. Subarray Sums Divisible by K (Medium)
def subarraysDivByK(self, A: List[int], K: int) -> int:
    res = 0
    subArrayCount = [1] + [0]*K
    prefix = 0
    for num in A:
        prefix = (prefix + num) % K
        # gives us a prefix number (i.e. modulus)
        # if we have seen it before, it means that up until the current number,
        # there are already subArrayCount[prefix] number of subarrays whose sums are divisible by K, so we add that number to our result
        res += subArrayCount[prefix]
        # update the count of subarrays with the prefix divisible by K
        subArrayCount[prefix] += 1

    return res

# Time complexity: O(N)
# Space complexity: O(N)

# 560. Subarray Sum Equals K (Medium)
def subarraySum(self, nums: List[int], k: int) -> int:
    contiguousSum = {0 : 1}

    sum = 0
    count = 0
    for num in nums:
        sum += num
        if (sum - k) in contiguousSum:
            count += contiguousSum[sum - k]
        contiguousSum[sum] = contiguousSum.get(sum, 0) + 1

    return count

# Time complexity: O(N)
# Space complexity: O(N)

# Explanation: Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum.
# If the same sum occurs again, we increment the count corresponding to that sum in the hashmap.
# Further, for every sum encountered, we also determine the number of times the sum (sum - k) has occured already,
# since it will determine the number of times a subarray with sum k has occured upto the current index. We increment the
# count by the same amount.

# 3. Longest Substring Without Repeating Characters (Medium)
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) <= 1:
        return len(s)
    last_occurence = dict()
    res = -1
    start_pt = 0
    for idx in range(len(s)):
        char = s[idx]
        if char in last_occurence and last_occurence[char] >= start_pt:
            start_pt = last_occurence[char] + 1
        else:
            res = max(res, idx-start_pt+1)
        last_occurence[char] = idx

    return res

# Time complexity: O(N)
# Space complexity: O(N)