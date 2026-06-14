class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_altitude=0
        highest_altitude=0
        for i in gain:
            cur_altitude+=i
            highest_altitude=max(cur_altitude,highest_altitude)
        return highest_altitude