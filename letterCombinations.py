class Solution:
   def letterCombinations(self,digits):
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def generate_combinations(combination, remaining_digits, output):
            if not remaining_digits:
                output.append(combination)
                return

            digit = remaining_digits[0]
            letters = digit_to_letters[digit]

            for letter in letters:
                generate_combinations(combination + letter, remaining_digits[1:], output)

        combinations = []
        generate_combinations('', digits, combinations)
        return combinations
