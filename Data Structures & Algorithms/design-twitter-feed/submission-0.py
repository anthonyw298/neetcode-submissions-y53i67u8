class Twitter:
    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) #userId - set of followeeId
        self.tweetMap = defaultdict(list) #userId - list of [count,tweetId]

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        self.followMap[userId].add(userId)
        res, heap = [], []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap,(count,index - 1,tweetId,followeeId))
        while heap and len(res) < 10:
            count,index,tweetId,followeeId = heapq.heappop(heap)
            res.append(tweetId)
            if index>= 0:
                count, tweetId = self.tweetMap[followeeId][index] 
                heapq.heappush(heap,(count,index - 1,tweetId,followeeId))
        return res
            

            



    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

