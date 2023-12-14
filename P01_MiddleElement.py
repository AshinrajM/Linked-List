class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Latest:
    def __init__(self, value):
        sample = Node(value)
        self.head = sample
        self.tail = sample
        self.length = 1

    def Append(self, value):
        sample = Node(value)
        if self.length == 0:
            self.head = sample
            self.tail = sample

        else:
            self.tail.next = sample
            self.tail = sample
        self.length += 1
        return True

    def Middle(self):
        if self.length==0 or self.length==1 or self.length==2:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value



abc = Latest(5)
abc.Append(78)
abc.Append(56)
abc.Append(67)
abc.Append(6)
abc.Append(7)
abc.Append(7)
# abc.Append(89)
print(abc.Middle())
