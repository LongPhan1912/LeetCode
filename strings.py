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
