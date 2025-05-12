class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        evens = [d for d in cnt if d % 2 == 0]
        res = set()

        # a = hundreds place (≠0), b = tens place, c = ones place (even)
        for a in cnt:
            if a == 0:                   # no leading zero
                continue
            for b in cnt:
                # need at least two of the same digit if a==b
                if a == b and cnt[b] < 2:
                    continue
                for c in evens:
                    # build a small counter of how many times we use each digit
                    need = Counter((a, b, c))
                    # check availability
                    if all(cnt[d] >= need[d] for d in need):
                        res.add(100*a + 10*b + c)

        return sorted(res)