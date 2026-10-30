class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split('/')
        res = []
        res.append('/')
        for i in range(1, len(items)):
            if(items[i] == '' or items[i] == '.'):
                continue
            elif(items[i] == '..'):
                if(len(res) > 2):
                    res.pop()
                    res.pop()
                else:
                    continue
            else:
                res.append(items[i])
                res.append('/')
        if (len(res) > 1):
            res.pop()
        return "".join(res)