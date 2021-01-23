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