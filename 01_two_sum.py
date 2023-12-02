
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Учитывая массив целых чисел nums и целочисленную цель, верните индексы двух чисел таким образом, чтобы они складывались в target.
Вы можете предположить, что каждый ввод будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
Вы можете возвращать ответ в любом порядке.
https://dzen.ru/a/ZSaLOGest2rIWdAT разбор задачки.
'''

# from ast import List
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        # print(target)        
        for id in range(len(nums) - 1):            
            for second_id in range(id + 1, len(nums)):
                if nums[second_id] == target - nums[id]:
                    return [id, second_id]
        
    

if __name__ == '__main__':
    sol = Solution()    
    print(sol.twoSum(nums=[-3,4,3,90], target=0))