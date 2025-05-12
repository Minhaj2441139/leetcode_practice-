class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = {
        100*a + 10*b + c
        for a, b, c in permutations(digits, 3)
        if a != 0      # no leading zero
        and c % 2 == 0 # last digit even
    }
    return sorted(result)