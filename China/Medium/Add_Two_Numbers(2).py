# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_bw = l1[::-1] # Otocil
        l2_bw = l2[::-1]

        l1_str = ''.join(str(number) for number in l1_bw) # Zmenil na str, int neslo
        l2_str = ''.join(str(number) for number in l2_bw)

        sucet = int(l1_str) + int(l2_str) # zmenil na int a spocital
        sucet_str = str(sucet) # zmenil zase na STR, aby som spravil lit

        sucet_bw = list((sucet_str[::-1]))

        return sucet_bw


print(Solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))
