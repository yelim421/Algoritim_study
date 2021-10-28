class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge = [set() for _ in range(n)]
        for i, j in edges :
            edge[i].add(j)
            edge[j].add(i)
        print(edge)
        q = [x for x in range(n) if len(edge[x]) < 2] #빼야됨
        temp = []
        print(q)
        while True:
            for node in q:
                for n in edge[node]:
                    edge[n].remove(node)
                    if len(edge[n]) == 1:
                        temp.append(n)
            if not temp: break
            temp, q = [], temp
        return q