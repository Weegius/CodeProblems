class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return ['']
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        first_digit = digits[0]
        rest_digits = digits[1:]
        rest_combinations = self.letterCombinations(rest_digits)
        result = []
        for letter in letters[first_digit]:
            for rest_combination in rest_combinations:
                result.append(letter + rest_combination)
        return result
