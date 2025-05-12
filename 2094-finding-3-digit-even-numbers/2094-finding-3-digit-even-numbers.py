class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result = set()
        
        # Try every choice of 3 distinct positions i, j, k
        for i in range(n):
            d1 = digits[i]
            if d1 == 0:               # leading zero → skip
                continue
            for j in range(n):
                if j == i:
                    continue
                d2 = digits[j]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    d3 = digits[k]
                    if d3 % 2 != 0:    # must be even
                        continue
                    num = d1 * 100 + d2 * 10 + d3
                    result.add(num)
        
        return sorted(result)