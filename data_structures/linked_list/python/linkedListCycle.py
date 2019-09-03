# Leetcode 142

'''SLOW, EXTRA SPACE'''
def detectCycleExtraSpace(self, head):
    if head == None: return None
    seen = [head]
    cur = head.next
    
    while cur != None:
        if cur in seen: 
            return cur
        seen.append(cur)
        cur = cur.next
        
    return None

'''VERY SLOW, NO EXTRA SPACE'''
def detectCycleNoExtraSpaceSlow(self, head):
    cur = head
    while cur != None:
        # return if node points to itself
        if cur == cur.next: return cur

        # store temp iterator node
        temp = head
        while temp != cur:
            if temp = cur.next:
                return temp
            temp = temp.next
        cur = cur.next
    return None


'''
                  LOOP   _____
   HEAD           ENTRY /     ()  <-- MEET POINT
    ()-----------------()      | 
                        \______/

    SET TWO POINTERS:
        - slow (move one at a time)
        - fast (move two at a time)
    If there is a loop, these two will eventually meet somewhere within the loop.

    From HEAD to LOOP ENTRY       = h  steps
    From LOOP ENTRY to MEET POINT = e  steps
    From MEET POINT to LOOP ENTRY = m  steps
    e + m = 1 full cycle

    FAST will NECESSARILY pass the meeting point at least once, because SLOW needs
    to catch up
        HENCE: the distance covered by FAST is:
            h + e + m + e + x(e + m)    - where x is some constant number of loops (e + m)

    SLOW  moves at half the rate of FAST, therefore:
            h + e + y(e + m)  - where y is some constant number of loops (e + m)
            EQUALS
            2 * (h + e + m + e + x(e + m))

            or more simply:

            h + 2e + m + x(e + m) = 2h + 2e + 2y(e + m)
           -h                       -h
               -2e                      -2e
            ___________________________________________

            m + x(e + m)   = h + 2y(e + m)

            m + x(circles) = h + y(circles)

            SO:
            remembering that 
                - h is the distance from HEAD to LOOP ENTRY
                - m is the distance from MEET POINT to LOOP ENTRY

            We don't need to worry about the number of circles, because if we
            start one pointer at m and another at h, no matter how many
            (constant number of) circles each must do they, will both meet at
            the entry

    - We aleady know h (head)
    - We can find m (meet) -- if it exists -- using the previously discussed 
      slow fast approach

    - Knowing both, all we need to do is increment each by one until they meet
    - and that meeting point is the loop entry!
'''

def detectCycleNoExtraSpaceTwoPointers(self, head):
    if head == None: return None

    slow = head
    fast = head
    isCycle = False

    # find collision point
    while slow != None and fast != None: 
        slow = slow.next

        if fast.next == None: return None
        else: fast = fast.next.next
        if slow = fast:
            isCycle = True
            break

    if not isCycle: return None
    fromHead = head
    fromMeet = slow
    while fromHead != fromMeet:
        fromHead = fromHead.next
        fromMeet = fromHead.next
    return fromHead


def otherDetectCycleNoExtraSpaceTwoPointer(head):
    slow = fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


