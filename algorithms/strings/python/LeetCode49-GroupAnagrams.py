import time
import tracemalloc
from typing import List

#------------------------------------------------------------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashValue(input: str) -> str:
            # Create an array of 26 zeros to count occurrences of each character
            alphabet_count = [0] * 26
    
            # Count the occurrences of each character
            for char in input:
                index = ord(char) - ord('a')  # Get the index of the character
                alphabet_count[index] += 1  # Increment the count for the character
    
            # Convert the character counts to a tuple (immutable, hashable)
            return tuple(alphabet_count)

        hashmap = {}
        for word in strs:
            key = hashValue(word)
            if key not in hashmap:
                hashmap[key] = []  # Initialize as an empty list
            hashmap[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(hashmap.values())
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

    # Test Case 1: Basic anagram groups
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.groupAnagrams(strs)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected_output]), f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 1 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 2: Single word
    strs = ["abc"]
    expected_output = [["abc"]]
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.groupAnagrams(strs)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 2 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 3: All words are the same
    strs = ["abc", "abc", "abc"]
    expected_output = [["abc", "abc", "abc"]]
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.groupAnagrams(strs)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 3 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 4: Empty input
    strs = []
    expected_output = []
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.groupAnagrams(strs)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 4 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 5: Large input according to constraints
    strs = [
        "a" * 100,  # String of length 100
        "b" * 100,  # Another large string (length 100)
        "a" * 99 + "b"  # Another large string (length 100)
    ] * 125 

    # Expected output: Anagrams grouped together
    expected_output = [
        ["a" * 100] * 125,
        ["b" * 100] * 125,
        ["a" * 99 + "b"] * 125
    ]

    tracemalloc.start()
    start_time = time.time()
    result = solution.groupAnagrams(strs)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected_output]), f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 5 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

run_tests()
