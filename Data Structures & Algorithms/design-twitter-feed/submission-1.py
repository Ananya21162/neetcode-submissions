class Twitter:

    def __init__(self):
        self.count = 0
        self.userTweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # top 10 most recent feeds
        minHeap = []

        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            index = len(self.userTweets[followee])-1
            if index >= 0:
                count, tweetId = self.userTweets[followee][index][0], self.userTweets[followee][index][1]
                heapq.heappush(minHeap,[count,tweetId,followee, index])
        
        while len(res) < 10 and minHeap:
            _,tweetId,followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.userTweets[followee][index-1][0],self.userTweets[followee][index-1][1]
                heapq.heappush(minHeap,[count,tweetId,followee, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
