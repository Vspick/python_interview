
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s

        longest_palindromic = s[0]
        dp = [[True for _ in range(l)] for _ in range(l + 1)]
        print(dp)
        for start in range(l - 1):
            dp[2][start] = s[start] == s[start + 1]
            if dp[2][start]:
                longest_palindromic = s[start: start + 2]

        for length in range(3, l + 1):
            for start in range(l - length + 1):
                end = start + length - 1
                print(dp[length - 2][start + 1])
                dp[length][start] = dp[length - 2][start + 1] and s[start] == s[end]
                print(s[start: end + 1], dp[length][start], s[start], s[end])
                if dp[length][start]:
                    longest_palindromic = s[start:start + length]
        return longest_palindromic


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        maxlen = 1
        start = 0
        for i in xrange(len(s)):
            if i - maxlen >= 1 and s[i - maxlen - 1:i + 1] == s[i - maxlen - 1:i + 1][::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and s[i - maxlen:i + 1] == s[i - maxlen:i + 1][::-1]:
                start = i - maxlen
                maxlen += 1

        return s[start:start + maxlen]


if __name__ == "__main__":
    obj = Solution()
    r = obj.longestPalindrome("babad")
    print(r)

