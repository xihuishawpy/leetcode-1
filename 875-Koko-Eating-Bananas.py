class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = sum(((p-1)//m) + 1 for p in piles)
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
