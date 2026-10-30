class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord('a')] += 1

            key = tuple(counter)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())