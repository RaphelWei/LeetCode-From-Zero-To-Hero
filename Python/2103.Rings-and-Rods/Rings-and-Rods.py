class Solution:
    def countPoints(self, rings: str) -> int:
        a = [0] * 10
        n = len(rings)
        for i in range(0,n,2):
            if rings[i] == 'R':
                a[int(rings[i+1])] |= 1
            elif rings[i] == 'G':
                a[int(rings[i+1])] |= 2
            else:
                a[int(rings[i+1])] |= 4

        count = 0
        for x in a:
            if x == 7:
                count += 1

        return count


rings = "B0B6G0R6R0R6G9"
sol = Solution()
print(sol.countPoints(rings))