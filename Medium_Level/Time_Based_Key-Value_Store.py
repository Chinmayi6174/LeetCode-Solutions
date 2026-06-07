import bisect
class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        # Binary search on timestamps directly
        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        if i == 0:
            return ""
        return arr[i - 1][1]
