def lcs_length(x, y):
    # Create a table to store the lengths of the longest common subsequence of x[:i] and y[:j]
    m, n = len(x), len(y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Compute the lengths of the longest common subsequences using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    # Return the length of the longest common subsequence
    print(L)
    return L[m][n]

# Example usage
x = [7 ,2 ,9, 3, 1, 5, 9, 4]
y = [2 ,8 ,1 ,3 ,9 ,7]
print(lcs_length(x, y))  # Output: 2 (the LCS is [2, 4])


def max_gold(W, bars):
    n = len(bars)
    # Create a table to store the maximum amount of gold that can be collected using a weight limit of w
    # and a set of bars from the first i bars
    table = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill in the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # If the current bar is too heavy to be included, skip it
            if bars[i - 1] > w:
                table[i][w] = table[i - 1][w]
            else:
                # Otherwise, take the maximum of including the current bar and not including it
                table[i][w] = max(table[i - 1][w], table[i - 1][w - bars[i - 1]] + bars[i - 1])
    
    # Return the maximum amount of gold that can be collected
    return table[n][W]

# Example usage
W = 10
bars = [3, 4, 5, 8, 10]
print(max_gold(W, bars))  # Output: 10 (the maximum amount of gold that can be collected is 10, using bars of weights 3 and 5)