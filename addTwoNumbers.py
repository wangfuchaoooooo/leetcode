# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        carry = 0
        rear = result

        while l1 or l2:

            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            sum_num = l1.val + l2.val + carry
            rear.next = ListNode(sum_num % 10)
            rear = rear.next
            carry = sum_num // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            rear.next = ListNode(1)

        return result.next

    def create_list_node(self, list_):
        result = ListNode(0)
        temp = result
        for i in list_:
            temp.next = ListNode(i)
            temp = temp.next
        return result.next

    def print_list_node(self, list_node):
        while list_node is not None:
            if list_node.next is None:
                print(list_node.val)
            else:
                print(list_node.val, '->', end=' ')
            list_node = list_node.next


if __name__ == '__main__':
    t = Solution()
    x1 = t.create_list_node([9])
    x2 = t.create_list_node([9, 9, 9])
    y = t.addTwoNumbers(x1, x2)
    t.print_list_node(y)
