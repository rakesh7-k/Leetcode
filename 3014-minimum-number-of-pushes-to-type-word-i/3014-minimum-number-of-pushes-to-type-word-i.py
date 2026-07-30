class Solution:
    def minimumPushes(self, word: str) -> int:
        p=0
        for i in range(len(word)):
            p+=(i//8)+1
        return p