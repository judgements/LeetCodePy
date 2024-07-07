"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1, 则在该链表中没有环。注意: pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。
"""

import os, sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
    ans_node = head
    fast, slow = head, head
    while True:
        if not (fast and fast.next):
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    fast = head
    while True:
        fast = fast.next
        slow = slow.next
        if fast == slow:
            break
    ans_node = fast
    return ans_node


head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

ans_node = detectCycle(head)
if ans_node == None:
    print('null')
else:
    print(ans_node.val)
