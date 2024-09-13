import time
import tracemalloc

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#------------------------------------------------------------

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            
            left, right = left.next, right.next
        
        return True

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

# Helper function to convert list to linked list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def run_tests():
    solution = Solution()

    # Test Case 1: Simple Palindrome
    head = create_linked_list([1, 2, 2, 1])
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(head)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 1 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 2: Not a Palindrome
    head = create_linked_list([1, 2, 3, 4])
    expected_output = False
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(head)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 2 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 3: Single Element
    head = create_linked_list([1])
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(head)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 3 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 4: Empty Linked List
    head = create_linked_list([])
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(head)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 4 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Test Case 5: Large Palindrome List
    head = create_linked_list([1] * 5000 + [0] + [1] * 5000)  # Large palindrome list
    expected_output = True
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.isPalindrome(head)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Test Case 5 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

run_tests()
