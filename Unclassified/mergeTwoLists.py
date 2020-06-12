# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
                head = head.next
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2
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


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

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
    l1 = t.create_list_node([1, 2, 4])
    t.print_list_node(l1)
    l2 = t.create_list_node([1, 3, 4])
    t.print_list_node(l2)
    x = t.mergeTwoLists(l1, l2)
    t.print_list_node(x)
