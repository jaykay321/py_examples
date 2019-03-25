class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
    def __str__(self):
        return str(self.value)

def rev_link_list(head):
    cur = head
    ord = []

    while cur:
        ord.append(cur)
        cur = cur.nextnode
    ord = ord[::-1]
    for ll in ord:
        print(ll)

la = Node(1)
lb = Node(2)
lc = Node(3)
la.nextnode = lb
lb.nextnode = lc

print(rev_link_list(la))
