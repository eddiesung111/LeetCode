class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        count = 0
        for item in arr:
            if item not in map:
                map[item] = False # distinct
            else:
                map[item] = True # not distinct
        
        for item1 in arr:
            if map[item1] == False and count + 1 == k:
                    return item1
            elif map[item1] == False:
                count += 1
        return ""
