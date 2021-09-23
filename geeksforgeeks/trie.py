from copy import deepcopy


class TrieNode:
    def __init__(self, key: str):
        self.key = key
        self.end = False
        self.ref = [None] * 26
        self.pc = 0


class PrefixTree:
    def __init__(self):
        self.root = TrieNode('/')
        self.res = []

    @staticmethod
    def _char2index(ch) -> int:
        return ord(ch) - ord('a')

    def insert(self, data: str):
        curr = self.root

        for ch in data:
            index: int = self._char2index(ch)
            if not curr.ref[index]:
                curr.ref[index] = TrieNode(ch)
            curr = curr.ref[index]
            if curr:
                curr.pc += 1
        curr.end = True

    def search(self, data: str):
        curr = self.root

        for ch in data:
            index = self._char2index(ch)

            if (not curr) or (not curr.ref[index]):
                return False
            curr = curr.ref[index]

        if (not curr) or curr.end == False:
            return False

        return True

    def delete(self, data: str):
        curr = self.root

        if self.search(data):
            for ch in data:
                index = self._char2index(ch)

                if (not curr) or (not curr.ref[index]):
                    return
                curr = curr.ref[index]
                curr.pc -= 1

        if curr and curr.end == True:
            curr.end = False

    def getPrefixCount(self, prefix):
        curr = self.root

        for ch in prefix:
            index = self._char2index(ch)

            if (not curr) or (not curr.ref[index]):
                return 0
            curr = curr.ref[index]

        return curr.pc if curr else 0

    def getShortestPrefix(self):
        curr = self.root
        curr.pc = 0
        prefix = ['']*100
        self._go(curr, prefix, 0)

        return self.res

    def _go(self, root, prefix, idx):

        if not root: return

        if root.pc == 1:
            self.res.append(''.join(prefix[:idx]))
            return

        for i in range(26):
            if root.ref[i]:
                prefix[idx] = chr(ord('a') + i)
                self._go(root.ref[i], prefix, idx+1)


if __name__ == '__main__':
    words = ["a", "aa", "ab", "abc", "aab"]
    tr = PrefixTree()
    for word in words:
        tr.insert(word)

    print(tr.getPrefixCount('a'))
    print(tr.getPrefixCount('aa'))
    print(tr.getPrefixCount('b'))
    print(tr.getPrefixCount('aab'))
    print(tr.getShortestPrefix())
