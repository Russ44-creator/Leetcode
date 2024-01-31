'''
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = TrieNode()
                node = node.children[w]
        node.isEnd = True

    def find(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return node.isEnd

    def startswith(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return True

class Solution:
    def findWords(self, board, words):
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)
        m, n = len(board), len(board[0])
        ans = []
        def dfs(r, c, node, word):
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] == " " or board[r][c] not in node.children):
                return
            temp_char = board[r][c]
            board[r][c] = " "
            word += temp_char
            node = node.children[temp_char]
            if node.isEnd:
                ans.append(word)
                node.isEnd = False # 剪枝
            if not node.children:
                del node
            else:
                dfs(r + 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c - 1, node, word)
            board[r][c] = temp_char

        for i in range(m):
            for j in range(n):
                dfs(i, j, word_trie.root, "")
        
        return ans
