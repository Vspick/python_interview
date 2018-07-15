class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = {"1": ["I", "V", "X"],
                "10": ["X", "L", "C"],
                "100": ["C", "D", "M"],
                "1000": ["M", "", ""]}

        convert = ""
        factor = 1
        while num > 0:
            cur_n = num % 10
            one, five, ten = base[str(factor)]
            if cur_n <= 3:
                cur_c = one * cur_n
            elif cur_n == 4:
                cur_c = one + five
            elif cur_n == 5:
                cur_c = five
            elif cur_n < 9:
                cur_c = five + (cur_n - 5) * one
            else:
                cur_c = one + ten
            convert = cur_c + convert

            num = int(num / 10)
            factor *= 10
        return convert


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {0: ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
                1: ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
                2: ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                3: ('', 'M', 'MM', 'MMM')}
        roman = ''
        roman += dict[3][int(num/1000) % 10]
        roman += dict[2][int(num/100) % 10]
        roman += dict[1][int(num/10 % 10)]
        roman += dict[0][int(num % 10)]

        return roman
