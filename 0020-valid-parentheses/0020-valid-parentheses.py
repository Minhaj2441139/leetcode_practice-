class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={")":"(","}":"{","]":"["}

        for c in s:
            if c in map:
                if stack and stack[-1]==map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True