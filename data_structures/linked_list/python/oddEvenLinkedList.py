# Leetcode 328

class ListNode:
    def __init__(self, val):
        self.val = val  
        self.next = None


# using four pointers
def pointersOddEvenList(self, head):
   
    if head == None: return head # head is pointer 1 
    odd = head                   # odd is pointer 2
    even = head.next             # even is pointer 3 
    evenHead = even              # evenHead is pointer 4

    # while another even and odd exist
    while even != None and even.next != None:
        # current odd POINTS TO next odd
        odd.next = even.next                                                  
        # currend odd BECOMES next odd
        odd = odd.next

        # current even POINTS TO next even
        even.next = odd.next
        # current even BECOMES next even
        even = even.next
    
    # combine the lists
    odd.next = evenHead
    return head


# using dummy nodes as pointers
def dummyOddEvenList(self, head):
    # initialize odd, even, and dummies whose only important value is what 
    # they will point to (not their stored value)
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
   
    while head: # we don't have to keep a pointer to head, cuz dummy 1
        odd.next = head
        odd = odd.next

        even.next = head.next
        even = even.next

        # only point head at next odd if there was an even before it
        head = head.next.next if even else None

    # point last odd to first even, which is what dummy 2 points at
    odd.next = dummy2.next
    # return head of odds, which is what dummy1 points at
    return dummy1.next
