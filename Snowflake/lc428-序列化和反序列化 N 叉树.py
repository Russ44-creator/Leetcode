"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root == None:
            return ""
        data = ""
        data += str(root.val) + '#'
        #结点#儿子1，儿子2，儿子3#”
        Q = collections.deque()
        Q.append(root)
        while Q:
            t = Q.popleft()
            for child in t.children:
                data += str(child.val) + ','
                Q.append(child)
            data += '#'
        return data
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == "":
            return None
        dataLen = len(data)
        ID = 0
        val = 0
        while ID < dataLen and data[ID].isdigit():
            val = val * 10 + int(data[ID])
            ID += 1
        root = Node(val)
        ID += 1         #跳过'#'
        Q = collections.deque()
        Q.append(root)
        while Q and ID < dataLen:
            t = Q.popleft()
            t.children = []
            while ID < dataLen and data[ID] != '#':
                val = 0
                while ID < dataLen and data[ID].isdigit():
                    val = val * 10 + int(data[ID])
                    ID += 1
                child = Node(val)
                ID += 1         #跳过','
                t.children.append(child)
                Q.append(child) 
            ID += 1             #跳过'#'

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
