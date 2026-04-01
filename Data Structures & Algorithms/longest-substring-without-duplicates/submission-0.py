# BRUTE FORCE
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        for i in range(len(s)):
            count=0
            seen_char=set()
            for j in range(i,len(s)):
                char=s[j]
                if char in seen_char:
                    break
                seen_char.add(char)
                count+=1
                
                max_count=max(count,max_count)
        return max_count
