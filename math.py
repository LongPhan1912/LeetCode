# 1346. Check If N and Its Double Exist (Easy)
def checkIfExist(self, arr: List[int]) -> bool:
    doubleDict = {}
    for num in arr:
        doubleDict[num] = doubleDict.get(num, 0) + 1
    
    if 0 in doubleDict and doubleDict[0] > 1:
        return True
    
    for num in arr:
        if num != 0:
            if (num*2 in doubleDict) or (num % 2 == 0 and (num / 2) in doubleDict):
                return True
    
    return False

# Time complexity: O(n)
# Space complexity: O(n)

# 1323. Maximum 69 Number (Easy)
def maximum69Number (self, num: int) -> int:
    sum = 0
    n = 3
    visited = False
    while (n >= 0):
        tens = 10**n
        digit = num // tens
        num = num % tens
        if digit == 6 and not visited:
            sum += 9*tens
            visited = True
        else:
            sum += digit*tens
        n -= 1
        
    return sum

# Time complexity: O(n)
# Space complexity: O(1)