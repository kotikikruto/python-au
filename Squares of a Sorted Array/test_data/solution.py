from typing import List


class Solution:
    def merge(self, fl, sl):
        f = 0
        s = 0
        result = []
        while f < len(fl) and s < len(sl):
            if fl[f] < sl[s]:
                result.append(fl[f])
                f += 1
            else:
                result.append(sl[s])
                s += 1
        while f < len(fl):
            result.append(fl[f])
            f += 1
        while s < len(sl):
            result.append(sl[s])
            s += 1
        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        i = 0
        while i < len(nums) and nums[i] < 0:
            lst1.append(nums[i])
            i += 1
        while i < len(nums):
            lst2.append(nums[i])
            i += 1
        lst11 = []
        lst22 = []
        for j in range(len(lst1)):
            lst11.append(lst1[len(lst1) - j - 1] ** 2)
        for j in range(len(lst2)):
            lst22.append(lst2[j] ** 2)
        return self.merge(lst11, lst22)
