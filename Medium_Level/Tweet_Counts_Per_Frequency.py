class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)
    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.tweets[tweetName], time)
    def getTweetCountsPerFrequency(
        self,
        freq: str,
        tweetName: str,
        startTime: int,
        endTime: int
    ) -> List[int]:
        interval = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }[freq]
        buckets = (endTime - startTime) // interval + 1
        ans = [0] * buckets
        times = self.tweets[tweetName]
        left = bisect_left(times, startTime)
        right = bisect_right(times, endTime)
        for t in times[left:right]:
            idx = (t - startTime) // interval
            ans[idx] += 1
        return ans
