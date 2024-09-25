def matches(message, pattern):
    
    dp = [[False] * (len(pattern) + 1) for _ in range(len(message) + 1)]
   
    dp[0][0] = True

   
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len(message) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == '*':
               
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len(message)][len(pattern)]


print(matches("aa", "a"))      
print(matches("aa", "*"))      
print(matches("cb", "?a"))     
print(matches("adceb", "*a*b")) 
print(matches("acdcb", "a*c?b")) 
