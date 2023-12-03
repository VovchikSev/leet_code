
'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.\
    
Учитывая массив положительных целых чисел nums и target положительное целое число, верните минимальную длину
подмассива, сумма которого больше или равна целевому. Если такого подмассива нет, верните вместо него 0.

разбор задачи https://www.youtube.com/watch?v=poABbx9oyeY
Решить через пару указателей

'''
import time
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = r = 0
        toatl = 0
        for l in range(len(nums)):
            toatl +=  nums[r]
            while toatl >= target:
                res = min(r - 1 + l,  res)
                toatl -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
        
        
    

if __name__ == '__main__':
    sol = Solution()    
    tic = time.perf_counter()
    print(sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(f"Вычисление заняло {time.perf_counter() - tic:0.4f} секунд")