class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money

            maximum = max(maximum, total)

        return maximum