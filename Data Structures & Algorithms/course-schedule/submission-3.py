class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Attempt 3
        #2 elements per sublist? index idx 0 depends on 1. Can prereq be empty? Only numbers or can be letters?multiple compenents?
        #Brute - Not Sure maybe check all the nodes and it correlation not sure how that would look
        #Optimal - use graphs traversing thru prereq and creating a adj list and thend fs to run thru ensuring no cycles
        #cycle detection problem complexity brute: not sure optimal : O(v+e) and space O(V+E) cant explain as well tho
        
        #key course and value:[list of prereqs]
        adj={i:[] for i in range(numCourses)}
        visit=set()
        #build adjlist
        for course,prereq in prerequisites:
            adj[course].append(prereq)
        #run dfs to ensure no cycles
        def dfs(course,path):
            #base case
            if course in path:
                return False
            path.add(course)
            if course not in visit:
                for i in adj[course]:
                    if not dfs(i,path):
                        return False
            path.remove(course)
            if course not in visit:
                visit.add(course)
            return True

            #recurse

        for course in adj:
            if not dfs(course,set()):
                return False
            #potential visit append 
        if len(visit)==numCourses:
            return True
        return False
        #compare to numcourses


        


































        #Attempt 2
        '''preMap= {}
        for i in range(numCourses):
            preMap[i]=[]
        for i,j in prerequisites:
            preMap[i].append(j)
        visit=set()
        def dfs(c):
            if c in visit:
                return False
            visit.add(c)
            for i in preMap[c]:
                if not dfs(i):
                    return False
            visit.remove(c)
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True'''
        
        #Attempt 1
        '''if len(prerequisites)==0:
            return True
        pre=set()
        post=set()
        def dfs(i,num):
            
            if num>=numCourses and i==len(prerequisites):
                return True
            #False Case
            print(i)
            arr = prerequisites[i]
            if arr[1] in post and arr[0] in pre:
                return False
            if arr[1] not in pre:  
                pre.add(arr[1])
                num+=1
            if arr[0] not in post:
                post.add(arr[0])
                num+=1
            return dfs(i+1,num)  
        return dfs(0,0)'''

    
