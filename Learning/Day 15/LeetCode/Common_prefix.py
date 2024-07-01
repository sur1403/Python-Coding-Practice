class Solution(object):
    def common_prefix(self, strs):
        strs.sort()

        first = strs[0]
        last = strs[-1]
        com_pre = []


        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                com_pre.append(first[i])
        return com_pre

strs = ["flower","flow","flight", "surbhi", "flows", "flip", "farm"]
solution = Solution()
print(solution.common_prefix(strs))

 