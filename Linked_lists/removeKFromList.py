class ListNode:
  def __init__(self, value=None):
    self.value = value
    self.next = None

node0 = ListNode(3)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2
node0.next = node1
#[3, 1, 2, 3, 4, 5]

def removeKFromList(l, k):
  if l:
    current = l
    res = []

    while current.value == k and current.next != None:
      current = current.next
    if current.value == k and current.next == None:
      return None

    res.append(current.value)

    while current.next != None:
      if current.next.value == k:
        deleted = current.next
        current.next = deleted.next
      else:
        current = current.next
        res.append(current.value)
    
    return print(res)

  return print([])

removeKFromList(node0, 3)