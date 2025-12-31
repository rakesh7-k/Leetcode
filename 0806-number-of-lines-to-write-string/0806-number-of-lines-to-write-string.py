class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        mapp = {}
        for i in range(len(widths)):
            mapp[chr(i + 97)] = widths[i]
        
        # print(mapp)
        count = 1
        store = 0
        for i in s:
            if store + mapp[i] > 100:
                store = mapp[i]
                count += 1
            else:
                store += mapp[i]
        
        return [count, store]