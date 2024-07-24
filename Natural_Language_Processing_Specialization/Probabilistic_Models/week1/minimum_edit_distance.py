def minimum_edit_distance(word1: str, word2: str)->int:

    dp = [[0 for i in range(len(word2) + 1)] for i in range(len(word1) + 1)]

    for i in range(1, len(word1) + 1):
        dp[0][i] = dp[0][i - 1] + 1
    
    for i in range(1, len(word2) + 1):
        dp[i][0] = dp[i - 1][0] + 1


    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            insert_cost = dp[i][j - 1] + 1
            delete_cost = dp[i - 1][j] + 1
            replace_amount = 0 if word1[i - 1] == word2[j - 1] else 2
            replace_cost = dp[i - 1][j - 1] + replace_amount
            dp[i][j] = min(min(insert_cost, delete_cost), replace_cost)

    return dp[-1][-1]