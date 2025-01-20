"""
Leetcode Problem: 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of 
the longest valid (well-formed) parentheses substring.

"""

def longestValidParentheses(s: str) -> int:
        maxLength = 0
        left = right = 0

        # Left to Right traversal
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        # Right to Left traversal
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left = right = 0

        return maxLength
    
    
def main():
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()(()", 2),
        ("(()())", 6),
        ("())((())", 4),
        ("()()()", 6),
        ("(((", 0),
        (")))", 0),
        ("()(()))))", 6)
    ]
    
    headers = ["Test Case", "Input s", "Expected Output", "Actual Output", "Status"]
    col_widths = [len(header) for header in headers]
    
    data_rows = []
    passed = 0
    failed = 0
    
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = longestValidParentheses(s)
        status = "Passed" if result == expected else "Failed"
        if status == "Passed":
            passed += 1
        else:
            failed += 1
        safe_s = s.replace("|", "\\|")
        safe_expected = str(expected).replace("|", "\\|")
        safe_result = str(result).replace("|", "\\|")
        row = [
            f"Test Case {idx}",
            f"s: '{safe_s}'",
            f"Expected: {safe_expected}",
            f"Output: {safe_result}",
            status
        ]
        data_rows.append(row)
        for i, cell in enumerate(row):
            if len(cell) > col_widths[i]:
                col_widths[i] = len(cell)
    
    separator = " | "
    header_line = separator.join([headers[i].ljust(col_widths[i]) for i in range(len(headers))])
    separator_line = "-+-".join(['-' * col_widths[i] for i in range(len(headers))])
    
    print(header_line)
    print(separator_line)
    
    for row in data_rows:
        print(separator.join([row[i].ljust(col_widths[i]) for i in range(len(headers))]))
    
    print("\nSummary:")
    print(f"Total Test Cases: {len(test_cases)}, Passed: {passed}, Failed: {failed}")

if __name__ == "__main__":
    main()