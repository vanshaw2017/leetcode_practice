def longestPalindrome(s: str) -> str:
        if not s :
            return s
        # 维护一个数组，数组中每个元素表示以index i为中心或者左中心的回文
        res = "c"
        for i in range(len(s)):
             # 把它当成中心
            pre = i - 1
            next = i + 1
            # 把他当成左边的中心
            if i+1 < len(s):
                if s[i] == s[i+1]:
                    next = i+2
            # 把它当成中心
            pre = i - 1
            next = i + 1
            while pre >-1 and next< len(s):
                if s[pre] == s[next]:
                    pre = pre-1
                    next = next + 1
            res1 = s[pre+1:next-1]
            res = res if len(res)>len(res1) else res1
if __name__ == "__main__":
     longestPalindrome("aba")