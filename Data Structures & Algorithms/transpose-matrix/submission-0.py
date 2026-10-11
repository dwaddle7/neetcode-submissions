class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        for i in range(cols):
            res.append([])
            for j in range(rows):
                res[i].append(matrix[j][i])
        return res