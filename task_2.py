from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise TypeError("Вхідні данні мають бути списком рядків.")

        if not strings:
            return ""

        for i, word in enumerate(strings):
            self.put(word, i)

        prefix = ""
        node = self.root

        while node:
            if len(node.children) != 1 or node.is_end_of_word:
                break
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print(trie.find_longest_common_word(strings))
