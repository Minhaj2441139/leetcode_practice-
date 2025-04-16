class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        res = [0]*len(rooms)
        res[0]=1

        def dfs(node):
            for nrg in rooms[node]:
                if not res[nrg]:
                    res[nrg]=1
                    dfs(nrg)
        
        dfs(0)
        return all(res)
