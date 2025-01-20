"""
Leetcode 76 - Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".

The testcases will be generated such that the answer is unique.
"""

def minWindow(s: str, t: str) -> str:
    from collections import defaultdict

    # Frequency map for characters in t
    targetFreq = defaultdict(int)
    for char in t:
        targetFreq[char] += 1

    windowFreq = defaultdict(int)
    required = len(targetFreq)
    
    formed = 0
    leftPtr = 0
        
    minLength = float('inf')
    minStart = 0

    # Expand the window with the right pointer
    for rightPtr, char in enumerate(s):
        windowFreq[char] += 1

        # Check if current character satisfies the required frequency
        if char in targetFreq and windowFreq[char] == targetFreq[char]:
            formed += 1

        # Contract the window from the left as much as possible
        while leftPtr <= rightPtr and formed == required:
            windowSize = rightPtr - leftPtr + 1
            if windowSize < minLength:
                minLength = windowSize
                minStart = leftPtr

            leftChar = s[leftPtr]
            windowFreq[leftChar] -= 1
                
            if leftChar in targetFreq and windowFreq[leftChar] < targetFreq[leftChar]:
                formed -= 1
            leftPtr += 1

    # Return the smallest window or empty string
    return "" if minLength == float('inf') else s[minStart:minStart + minLength]


def main():
    
    test_cases = [
        # Each test case is a tuple: (s, t, expected_output)
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
        ("ab", "b", "b"),
        ("ab", "a", "a"),
        ("abca", "abc", "abc"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("aa", "aa", "aa"),
        ("abdecfghabc", "abc", "abc"),
        ("this is a test string", "tist", "t stri"),
        ("geeksforgeeks", "ork", "ksfor"),
        ("abc", "abc", "abc"),
        ("abc", "abcd", ""),
        ("ab", "b", "b"),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
        # Add more test cases as needed, ensuring t is non-empty
    ]
    
    # Determine column widths
    headers = ["Test Case", "Input s", "Input t", "Expected Output", "Actual Output", "Status"]
    # Initialize column widths with header lengths
    col_widths = [len(header) for header in headers]
    
    # Prepare data rows
    data_rows = []
    passed = 0
    failed = 0
    for idx, (s, t, expected) in enumerate(test_cases, 1):
        result = minWindow(s, t)
        status = "Passed" if result == expected else "Failed"
        if status == "Passed":
            passed += 1
        else:
            failed += 1
        # Replace any '|' in the input strings to prevent misalignment
        safe_s = s.replace("|", "\\|")
        safe_t = t.replace("|", "\\|")
        safe_expected = expected.replace("|", "\\|")
        safe_result = result.replace("|", "\\|")
        row = [
            f"Test Case {idx}",
            f"s: '{safe_s}'",
            f"t: '{safe_t}'",
            f"Expected: '{safe_expected}'",
            f"Output: '{safe_result}'",
            status
        ]
        data_rows.append(row)
        # Update column widths
        for i, cell in enumerate(row):
            if len(cell) > col_widths[i]:
                col_widths[i] = len(cell)
    
    # Create format string
    separator = " | "
    header_line = separator.join([headers[i].ljust(col_widths[i]) for i in range(len(headers))])
    separator_line = "-+-".join(['-' * col_widths[i] for i in range(len(headers))])
    
    print(header_line)
    print(separator_line)
    
    for row in data_rows:
        print(separator.join([row[i].ljust(col_widths[i]) for i in range(len(headers))]))
    
    # Summary
    print("\nSummary:")
    print(f"Total Test Cases: {len(test_cases)}, Passed: {passed}, Failed: {failed}")

if __name__ == "__main__":
    main()   