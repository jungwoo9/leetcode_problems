class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            if "".join(sorted(word)) not in anagrams:    
                anagrams["".join(sorted(word))] = [word]
                continue
            anagrams["".join(sorted(word))].append(word)
        return anagrams.values()