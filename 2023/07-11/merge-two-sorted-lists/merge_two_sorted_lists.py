class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def mergeTwoLists(self, list1, list2):
    if not list1 and not list2:
        return None
    
    if not list2:
        return list1
    
    if not list1:
        return list2

    if list1.val <= list2.val:
        tmp = list1
        list1 = list1.next

    else:
        tmp = list2
        list2 = list2.next
    
    return ListNode(tmp.val, self.mergeTwoLists(list1, list2))
