from collections import defaultdict


class SolutionV1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        char_map = defaultdict()
        word_map = defaultdict()
        for p, word in zip(pattern, words):
            if (p in char_map and char_map[p] != word) or (word in word_map and word_map[word] != p):
                return False
            char_map[p] = word
            word_map[word] = p
        return True


class SolutionV2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s, t = pattern, s.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
