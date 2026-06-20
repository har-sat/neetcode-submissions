class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def ser(s):
            l = [0]*26
            for c in s:
                l[ord('a') - ord(c)] += 1
            return ','.join(str(c) for c in l)
        res = defaultdict(list) 
        for s in strs:
            key = ser(s)
            res[key].append(s)
        return list(res.values())