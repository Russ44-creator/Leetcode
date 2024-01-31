class FileSystem:

    def __init__(self):
        self.trie={}

    def getNode(self,path):
        path = [i for i in path.split('/') if i]
        curNode = self.trie
        for p in path:
            if p not in curNode:
                curNode[p] = {}
            curNode = curNode[p]
        return [curNode,path]

    def ls(self, path: str) -> list:
        node, path = self.getNode(path)
        if 'content' in node:
            return [path[-1]]
        else:
            return sorted(list(node.keys()))

    def mkdir(self, path: str) -> None:
        self.getNode(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node,path = self.getNode(filePath)
        if 'content' not in node:
            node['content'] = content
        else:
            node['content'] += content

    def readContentFromFile(self, filePath: str) -> str:
        node, path = self.getNode(filePath)
        return node['content']