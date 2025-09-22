class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        dictSet = set(dictionary)
        # def startWith(string, substring):
        #     if len(string) < len(substring):
        #         return False
        #     return string.startswith(substring)
            
        # def recur(s, dictionary):
        #     if len(s) == 0:
        #         return True
        #     for str in dictionary:
        #         if startWith(s, str):
        #             if recur(s[len(str):], dictionary):
        #                 return True
        #     return False
            
        # return recur(s, dictionary)
        maxLen = 0 
        for word in dictionary:
            maxLen = max(maxLen, len(word))

        dp = {0:True}
        for i in range(len(s)):
            for j in range(i,max(i-maxLen-1,-1),-1):
                dp[i+1] = False
                if s[j:i+1] in dictSet and dp[j]:
                    dp[i+1] = True
                    break
        return dp[len(s)]
                    
                