class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"(":")", "{":"}", "[":"]"}
        stack=[]

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if stack==[] or mapping[stack.pop()]!=char:
                    return False

        return True if stack==[] else False
        
