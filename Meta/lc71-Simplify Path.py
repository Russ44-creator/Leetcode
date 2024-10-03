class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        ans_list = []
        for dir in dirs:
            if dir == "":
                continue
            elif dir == ".":
                continue
            elif dir == "..":
                if not ans_list:
                    continue
                ans_list.pop()
                continue
            else:
                ans_list.append(dir)
        return "/" + "/".join(ans_list)
