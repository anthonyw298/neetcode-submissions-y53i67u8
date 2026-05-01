class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
        for airport in adj:
            heapq.heapify(adj[airport])
        res = []
        def dfs(airport):
            while adj[airport]:
                node = heapq.heappop(adj[airport])
                dfs(node)
            res.append(airport)
            
        
        dfs("JFK")
        res.reverse()
        return res





































        '''adjList = defaultdict(list)
        for begin, end in tickets:
            adjList[begin].append(end)
        for key in adjList:
            heapq.heapify(adjList[key])
        res = []
        def dfs(airport):
            while adjList[airport]:
                small = heapq.heappop(adjList[airport])
                dfs(small)
            res.append(airport)

        
        dfs("JFK")
        res.reverse()
        return res'''

            