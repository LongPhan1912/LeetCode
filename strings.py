# 833. Find And Replace in String (Medium)
def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
    # go from right to left instead of left to right
    # not bother with the changing string length
    for idx, source, target in \
        sorted(zip(indexes, sources, targets), reverse=True):
        end = idx + len(source)
        if S[idx:end] == source:
            S = S[:idx] + target + S[end:]
    return S

# Time complexity: O(NQ) where N is the length of S, and we have Q replacement operations.
# Space complexity: O(1)

# 621. Task Scheduler (Medium)
def leastInterval(self, tasks: List[str], n: int) -> int:
    freq = dict()
    for char in tasks:
        freq[char] = freq.get(char, 0) + 1
    
    sorted_keys = sorted(freq, key=lambda x:freq[x])
    max_key = sorted_keys.pop()
    max_val = freq[max_key] - 1 
    # subtract one because we don't need to wait on last occurence
    
    idle_slots = max_val * n
    # starting number of idle slots
    for key in sorted_keys:
        # if we have freq[key] == freq[max_key], then just take max_val
        # since it's one less than freq[key]
        idle_slots -= min(max_val, freq[key])
    
    return len(tasks) + idle_slots if idle_slots > 0 else len(tasks)

# Time complexity: O(NlogN) due to sorting
# Space complexity: O(N) as we use the freq dict and the sorted_keys array

# 125. Valid Palindrome (Easy)
def isPalindrome(self, s: str) -> bool:
    if len(s) <= 1:
        return True
    
    fullStr = ""
    for char in s:
        if char.isalnum():
            fullStr += char.lower()
    
    ptr1 = 0
    ptr2 = len(fullStr) - 1
    while (ptr1 <= ptr2 and ptr1 < len(fullStr) and ptr2 >= 0):
        if fullStr[ptr1] == fullStr[ptr2]:
            ptr1 += 1
            ptr2 -= 1
        else:
            return False
    return True

# Time complexity: O(N)
# Space complexity: O(1)

# 5. Longest Palindromic Substring (Medium)
def centerExpand(self, s, left, right):
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    return right - left - 1

def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    if n == 2:
        return s if (s[0] == s[1]) else s[0]

    start, end = 0, 0
    for i in range(n):
        # check for even palindrome
        evenLen = self.centerExpand(s, i, i)
        # check for odd palindrome
        oddLen = self.centerExpand(s, i, i+1)
        best = max(evenLen, oddLen)
        if (best > end - start):
            start = i - (best-1)//2
            end = i + best//2

    return s[start:end+1]

# Time complexity: O(N^2)
# Space complexity: O(1)

