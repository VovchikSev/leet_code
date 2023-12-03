
"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру. Сложите два числа и верните сумму в виде связанного списка.
Вы можете предположить, что эти два числа не содержат никакого начального нуля, за исключением самого числа 0.
https://zazloo.ru/leetcode-tasks2/?ysclid=lpprm6tit7419980388

"""

import time
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass
    
    
if __name__ == '__main__':
    sol = Solution()    
    tic = time.perf_counter()
    print(sol.addTwoNumbers(nums=[-3,4,3,90], target=0))
    print(f"Вычисление заняло {time.perf_counter() - tic:0.4f} секунд")