"""
Bob has arranged N boxes in a straight line. Each box has a lowercase Latin 
character (from 'a' to 'z') written on it. Bob’s goal is to form a chain by 
selecting exactly one box for each letter so that the chain follows the 
increasing lexicographic order—that is, the chain must start with a box 
containing 'a', then a box containing 'b', continuing sequentially until it 
ends with a box containing 'z'.

To connect two consecutive boxes in the chain, Bob uses a piece of chain 
whose length is equal to the absolute difference of the positions of the two 
boxes. For example, if the box selected for letter 'a' is at position i and 
the box for letter 'b' is at position j, then the length of the chain segment 
needed to connect them is |i - j|.

Your task is to help Bob determine the minimum total length of chain required 
to connect the selected boxes in the specified order. In other words, you 
must choose one occurrence of each letter (from 'a' to 'z') such that the sum 
of the distances between consecutive letters in the chain is minimized.

Input Format:

The first line contains a single integer T, representing the number of test 
cases. Each test case consists of a single line containing a string S made up 
of lowercase Latin characters ('a' to 'z'). Note: It is guaranteed that every 
letter from 'a' to 'z' appears in S at least once. The string S may contain 
one or more occurrences of each character.

Output Format:

For each test case, print a single integer — the minimum total chain length 
required to form the desired sequence from 'a' to 'z'.

Sample Input : 
2
abcdefghijklmnopqrstuvwxyz
ceaabcdefghijklmnopqrstuvwxyz

Sample Output:
25
25

"""

import bisect

def get_letter_positions(s):
    """
    Constructs a mapping from each letter to a sorted list of indices 
    where that letter occurs in the string s.
    """
    positions = {chr(ord('a') + i): [] for i in range(26)}
    for idx, ch in enumerate(s):
        positions[ch].append(idx)
    return positions

def transition_dp(P, dp, Q):
    """
    Given the DP state (with positions P and corresponding costs dp) for the previous letter,
    computes the minimum cost to transition to each candidate position in Q for the current letter.
    
    Args:
        P (List[int]): Sorted positions for the previous letter.
        dp (List[int]): DP costs corresponding to positions in P.
        Q (List[int]): Sorted positions for the current letter.
        
    Returns:
        List[int]: New DP state for positions in Q.
    """
    m_prev = len(P)
    m_next = len(Q)
    
    # Build prefix and suffix arrays.
    prefix = [0] * m_prev  # prefix[j] = min_{i<=j} (dp[i] - P[i])
    suffix = [0] * m_prev  # suffix[j] = min_{i>=j} (dp[i] + P[i])
    
    prefix[0] = dp[0] - P[0]
    for j in range(1, m_prev):
        prefix[j] = min(prefix[j - 1], dp[j] - P[j])
    
    suffix[m_prev - 1] = dp[m_prev - 1] + P[m_prev - 1]
    for j in range(m_prev - 2, -1, -1):
        suffix[j] = min(suffix[j + 1], dp[j] + P[j])
    
    new_dp = [0] * m_next
    for i in range(m_next):
        x = Q[i]
        cost = float('inf')
        # Case 1: p <= x.
        j = bisect.bisect_right(P, x) - 1
        if j >= 0:
            cost = min(cost, prefix[j] + x)
        # Case 2: p >= x.
        j2 = bisect.bisect_left(P, x)
        if j2 < m_prev:
            cost = min(cost, suffix[j2] - x)
        new_dp[i] = cost
    return new_dp

def compute_min_chain_cost(s):
    """
    Computes the minimum total chain length required to form a chain from 'a' to 'z'
    by connecting boxes in lexicographic order.
    
    Args:
        s (str): The input string representing the arrangement of boxes.
        
    Returns:
        int: The minimum total chain length.
    """
    positions = get_letter_positions(s)
    # Initialize DP for the starting letter 'a' with cost 0.
    dp = [0] * len(positions['a'])
    P = positions['a']
    
    # Process letters from 'b' to 'z'.
    for ch in "bcdefghijklmnopqrstuvwxyz":
        Q = positions[ch]
        dp = transition_dp(P, dp, Q)
        P = Q
        
    return min(dp)

def process_test_cases():
    """
    Processes hardcoded test cases and prints the results.
    """
    test_cases = [
        "abcdefghijklmnopqrstuvwxyz",  # Test case 1: Single occurrence per letter.
        "qwertyuiopasdfghjklzxcvbnm",      # Test case 2: Random permutation of a-z.
        "aaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"  # Test case 3: Multiple occurrences.
    ]
    for i, s in enumerate(test_cases, 1):
        result = compute_min_chain_cost(s)
        print(f"Test case {i}: {result}")

if __name__ == '__main__':
    process_test_cases()
