# 1004. Max Consecutive Ones III (Medium)
def longestOnes(self, A: List[int], K: int) -> int:
    ptr1 = 0
    ptr2 = 0
    while (ptr1 < len(A)):
        if A[ptr1] == 0:
            K -= 1
        if K < 0:
            if A[ptr2] == 0:
                K += 1
            ptr2 += 1
        ptr1 += 1
        
    return ptr1 - ptr2

def longestOnes(self, A: List[int], K: int) -> int:
    ptr1 = 0
    for ptr2 in range(len(A)):
        K -= 1 - A[ptr2]
        if K < 0:
            K += 1 - A[ptr1]
            ptr1 += 1
        
    return ptr2 - ptr1 + 1

# Time complexity: O(N)
# Space complexity: O(1)

# 977. Squares of a Sorted Array (Easy)
def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 1:
        return [nums[0]**2]
    for idx in range(n):
        nums[idx] = nums[idx]**2
    
    ptr1, ptr2 = 0, n-1
    stack = []
    while ptr1 < n and ptr2 >= 0 and ptr1 <= ptr2:
        nums1 = nums[ptr1]
        nums2 = nums[ptr2]
        if nums1 < nums2:
            stack.append(nums2)
            ptr2 -= 1
        elif nums1 > nums2:
            stack.append(nums1)
            ptr1 += 1
        else:
            stack.append(nums1)
            if ptr1 != ptr2:
                stack.append(nums2)
            ptr1+=1
            ptr2-=1
            
    return stack[::-1]

# Time complexity: O(N)
# Space complexity: O(N)

# 845. Longest Mountain in Array (Medium)
def longestMountain(self, arr: List[int]) -> int:
    res = 0
    n = len(arr)
    if n < 3:
        return 0
    
    i, j = 0, 0
    while i < n-1:
        j = i
        if j < n-1 and arr[j] < arr[j+1]:
            while j < n-1 and arr[j] < arr[j+1]:
                j+=1
            if j < n-1 and arr[j] > arr[j+1]:
                while j < n-1 and arr[j] > arr[j+1]:
                    j+=1
                res = max(res, j - i + 1)
        i = max(i+1, j)

    return res
# Time complexity: O(N)
# Space complexity: O(1)

# 838. Push Dominoes (Medium)
def pushDominoes(self, dominoes: str) -> str:
    n = len(dominoes)
    if (n <= 1):
        return dominoes
    
    head, tail = 0, n-1
    forceList = [0]*n
    
    force = 0
    for idx, item in enumerate(dominoes):
        if item == 'R': 
            force = n
        elif item == 'L':
            force = 0
        else:
            force = max(force-1, 0)
        forceList[idx] += force
        
    for idx in range(n-1, -1, -1):
        item = dominoes[idx]
        if item == 'R':
            force = 0
        elif item == 'L':
            force = n
        else:
            force = max(force-1, 0)
        forceList[idx] -= force
    
    res = []
    for f in forceList:
        if f > 0:
            res.append('R')
        elif f < 0:
            res.append('L')
        else:
            res.append('.')

    return ''.join(res)

# Time complexity: O(N)
# Space complexity: O(N)

# Hardcoding:
def pushDominoes(self, dominoes: str) -> str:
    if len(dominoes) == 1:
        return dominoes
    while True:
        res = dominoes.replace('R.L', 'S')
        res = res.replace('.L', 'LL').replace('R.', 'RR')
        if res == dominoes:
            break
        else:
            dominoes = res
        
    return dominoes.replace('S', 'R.L')

# Time complexity: O(N)
# Space complexity: O(N)

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
# Space complexity: O(N)

# 344. Reverse String (Easy)
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    
    return s

# Time complexity: O(N)
# Space complexity: O(1)

# 283. Move Zeroes (Easy)
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
# Space complexity: O(1)

# 42. Trapping Rain Water (Hard)
def trap(self, arr: List[int]) -> int:
    i, j = 0, len(arr)-1
    res = 0
    leftMax, rightMax = 0, 0
    while (i < j):
        if arr[i] < arr[j]:
            if arr[i] >= leftMax:
                leftMax = arr[i]
            else:
                res += leftMax - arr[i]
            i+=1
        else:
            if arr[j] >= rightMax:
                rightMax = arr[j]
            else:
                res += rightMax - arr[j]
            j-=1
    
    return res

# Time complexity: O(N)
# Space complexity: O(1)

# 11. Container With Most Water (Medium)
def maxArea(self, height: List[int]) -> int:
    n = len(height)
    l, r = 0, n-1
    maxScore = 0
    
    while (l < r):
        curr = min(height[l], height[r]) * (r - l)
        maxScore = max(maxScore, curr)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
            
    return maxScore
# Time complexity: O(N)
# Space complexity: O(1)