import time
import tracemalloc

#------------------------------------------------------------
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        
        mp = [-1] * 32
        longestSubstring = 0
        
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        
        return longestSubstring
#------------------------------------------------------------

def format_memory_usage(current, peak):
    if current < 10**6:
        current_usage = f"{current / 10**3:.3f} KB"
    else:
        current_usage = f"{current / 10**6:.3f} MB"
    
    if peak < 10**6:
        peak_usage = f"{peak / 10**3:.3f} KB"
    else:
        peak_usage = f"{peak / 10**6:.3f} MB"
    
    return current_usage, peak_usage

def run_tests():
    solution = Solution()

    # Test Case 1: Simple string with all vowels
    s = "eleetminicoworoep"
    expected_output = 13
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.findTheLongestSubstring(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 1 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 2: No vowels in the string
    s = "bcdfghjklmnpqrstvwxyz"
    expected_output = len(s)
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.findTheLongestSubstring(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 2 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 3: Empty string
    s = ""
    expected_output = 0
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.findTheLongestSubstring(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 3 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 4: Repeating single vowel
    s = "aaaaaaa"
    expected_output = 6
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.findTheLongestSubstring(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 4 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 5: Large input
    s = "a" * 500 + "e" * 500 + "i" * 500 + "o" * 500 + "u" * 500
    expected_output = 2500  # Because no valid substrings satisfy the condition
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.findTheLongestSubstring(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 5 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

run_tests()
