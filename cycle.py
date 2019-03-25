class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

def detect_cycle(head):
"""
Check if cycle appears in linked list
"""
    marker1 = head
    marker2 = head

    while marker1 and marker2:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return True
    return False

la = Node(1)
lb = Node(2)
lc = Node(3)
ld = Node(4)

la.nextnode = lb
lb.nextnode = lc
lc.nextnode = ld
ld.nextnode = True

print(detect_cycle(la))
