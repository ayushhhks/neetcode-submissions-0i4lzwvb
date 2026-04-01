from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))   # sorted string as key    if u use only sorted it gives a list['a', 'c', 't'] like this
            groups[key].append(word)

        return list(groups.values())


#So instead of comparing words, I:
# Sorted each word
# Used that sorted word as a key in a dictionary
# Stored original words under that key
# 🔹 Step-by-Step with Your Example
# Input:
# ["act","pots","tops","cat","stop","hat"]
# We process one word at a time:
# 1️⃣ word = "act"
# Sorted → "act"
# Dictionary:
# {
#   "act": ["act"]
# }
# 2️⃣ word = "pots"
# Sorted → "opst"
# {
#   "act": ["act"],
#   "opst": ["pots"]
# }
# 3️⃣ word = "tops"
# Sorted → "opst"
# {
#   "act": ["act"],
#   "opst": ["pots", "tops"]
# }
# 4️⃣ word = "cat"
# Sorted → "act"
# {
#   "act": ["act", "cat"],
#   "opst": ["pots", "tops"]
# }
# 5️⃣ word = "stop"
# Sorted → "opst"
# {
#   "act": ["act", "cat"],
#   "opst": ["pots", "tops", "stop"]
# }
# 6️⃣ word = "hat"
# Sorted → "aht"
# {
#   "act": ["act", "cat"],
#   "opst": ["pots", "tops", "stop"],
#   "aht": ["hat"]
# }
# 🔹 Final Outpu
# We return:
# [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

# 🧠 In One Line
# I stopped comparing words with each other
# and instead grouped them by their sorted form.