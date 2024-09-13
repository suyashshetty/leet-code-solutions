from typing import List

class Solution:
    def isPalindrome(self, s:str) -> bool:
        left, right = 0, len(s) - 1

        while left < right :
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True

import time
import tracemalloc

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

    # Test Case 1: Simple palindrome with non-alphanumeric characters
    s = "A man, a plan, a canal: Panama"
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 1 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 2: Not a palindrome
    s = "race a car"
    expected_output = False
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 2 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 3: Single alphanumeric character (valid palindrome)
    s = "P"
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 3 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 4: Empty string (trivially a palindrome)
    s = ""
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 4 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 5: String with only non-alphanumeric characters
    s = "@@@"
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 5 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 6: Palindrome with numbers
    s = "12321"
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 6 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 7: Large input (should handle efficiently)
    s = "a" * 1000000 + "b" + "a" * 1000000
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(s)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 7 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

run_tests()

