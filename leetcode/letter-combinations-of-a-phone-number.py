class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        digit2char = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        results = [""]
        for d in digits:
            new_results = []
            for c in digit2char[d]:
                for res in results:
                    res += c
                    new_results.append(res)
            results = new_results
        return results