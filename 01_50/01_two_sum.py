
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Учитывая массив целых чисел nums и целочисленную цель, верните индексы двух чисел таким образом, чтобы они складывались в target.
Вы можете предположить, что каждый ввод будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
Вы можете возвращать ответ в любом порядке.
https://dzen.ru/a/ZSaLOGest2rIWdAT разбор задачки.
записываем в хэш таблицу разность target и текущего элемента цикла, 
которое соответственно должно быть равно второму числу, которое будет искаться дальше в цикле, 
когда пара находится, выдаём ответ.
'''

import time
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # создать словарь в котором по значению в массиве хрантся индексы значений в списке nums
        for idx in range(len(nums)):
            complement = target - nums[idx] # дополнение, разница между текущим значением и целевым значением
            if complement in hash_map:
                return [idx, hash_map[complement]]
            hash_map[nums[idx]] = idx 
        
        
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:        
        for id in range(len(nums) - 1):            
            for second_id in range(id + 1, len(nums)):
                if nums[second_id] == target - nums[id]:
                    return [id, second_id]    

if __name__ == '__main__':
    sol = Solution()  
    tic = time.perf_counter() 
    print(sol.twoSum_brute_force(nums=[-3,4,3,90], target=0))
    print(f"Вычисление заняло {time.perf_counter() - tic:0.4f} секунд")
    tic = time.perf_counter() 
    print(sol.twoSum(nums=[-3,4,3,90], target=0))
    print(f"Вычисление заняло {time.perf_counter() - tic:0.4f} секунд")    