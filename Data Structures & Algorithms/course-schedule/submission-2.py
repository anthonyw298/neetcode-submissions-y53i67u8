class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Attempt 2
        preMap= {}
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
        return True
        
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

    
