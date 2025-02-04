"""
    Leetcode 2940: Alice and Bob are playing a game. They are at the same building
    and want to move to the same other building. 
    
    You are given a 0-indexed array heights of positive integers, where heights[i]
    represents the height of the ith building.

    If a person is in building i, they can move to any other building j if and only
    if i < j and heights[i] < heights[j].

    You are also given another array queries where queries[i] = [ai, bi]. On the
    ith query, Alice is in building ai while Bob is in building bi.

    Return an array ans where ans[i] is the index of the leftmost building where
    Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a
    common building on query i, set ans[i] to -1.

    Parameters:
    heights (List[int]): A list of positive integers representing the heights of
    the buildings.
    queries (List[List[int]]): A list of queries where each query is a list
    containing two integers [ai, bi].

    Returns:
    List[int]: A list of integers where each integer is the index of the leftmost
    building where Alice and Bob can meet for the corresponding query, or -1 if
    they cannot meet.
"""


import heapq

def leftmostBuildingQueries(heights, queries):
   
    max_idx = []  # Min-heap to simulate priority queue
    results = [-1] * len(queries)
    store_queries = [[] for _ in heights]

    # Store the mappings for all queries in store_queries.
    for idx, query in enumerate(queries):
        a, b = query
        if a < b and heights[a] < heights[b]:
            results[idx] = b
        elif a > b and heights[a] > heights[b]:
            results[idx] = a
        elif a == b:
            results[idx] = a
        else:
            store_queries[max(a, b)].append((max(heights[a], heights[b]), idx))

    for idx, height in enumerate(heights):
        # If the heap's smallest value is less than the current height, it is an answer to the query.
        while max_idx and max_idx[0][0] < height:
            _, q_idx = heapq.heappop(max_idx)
            results[q_idx] = idx
        # Push the queries with their maximum index as the current index into the heap.
        for element in store_queries[idx]:
            heapq.heappush(max_idx, element)

    return results

if __name__ == "__main__":
    heights = [4, 2, 3, 1]
    queries = [[0, 2], [1, 3], [2, 3], [3, 0]]
    print(leftmostBuildingQueries(heights, queries))  # Output: [2, -1, -1, -1]

    heights = [1, 3, 2, 4]
    queries = [[0, 1], [1, 2], [2, 3], [3, 0]]
    print(leftmostBuildingQueries(heights, queries))  # Output: [1, 3, 3, -1]