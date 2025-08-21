class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key: str, value):
        if not isinstance(key, str):
            raise TypeError("Ключ має бути рядком.")

        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.value = value

    def get(self, key: str):
        if not isinstance(key, str):
            raise TypeError("Ключ має бути рядком.")

        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end_of_word else None
