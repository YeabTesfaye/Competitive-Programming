class Solution:
   def intToRoman(self,num: int) -> str:
        if num <= 0 or num >= 4000:
            return "Invalid input: Number should be between 1 and 3999."

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result += symbols[i]

        return result

