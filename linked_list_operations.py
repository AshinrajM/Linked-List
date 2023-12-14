# Here we created a Class Node for creation of new nodes only.
# Whenever we need a create a newnode we just need to make a call for this class.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        NewNode = Node(value)
        self.head = NewNode
        self.tail = NewNode
        self.length = 1

    def Display(self):
        current = self.head
        while current:
            print(
                current.value, "==>tail:", self.tail.value, "==>Head:", self.head.value
            )
            current = current.next

    def AddNode(self, value):
        NewNode = Node(value)
        if self.length == 0:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            self.tail = NewNode

        self.length += 1
        return True

    def PopNode(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        current = self.head
        while current.next != self.tail:
            current = current.next
        self.tail = current
        self.tail.next = None
        self.length -= 1

    def PrependNode(self, value):
        NewNode = Node(value)
        if self.length == 0:
            self.head = NewNode
            self.tail = NewNode
        elif self.length == 1:
            NewNode.next = self.head
            self.head = NewNode
            self.tail = self.head.next
        else:
            NewNode.next = self.head
            self.head = NewNode
        self.length += 1

    def PopFirstNode(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.length -= 1

    # Here we are identifying the node value which present at a specified index using index value
    def GetByIndex(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # Here setting value at a specified index
    def SetValueByIndex(self, value, index):
        current = self.GetByIndex(
            index
        )  # Have to use self.GetByIndex because its an instance of a class
        if current:
            current.value = value
            return True
        return False

    # To insert at a particular index
    def Insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.PrependNode(value)
        if index == self.length:
            return self.AddNode(value)
        NewNode = Node(value)
        current = self.GetByIndex(index - 1)
        NewNode.next = current.next
        current.next = NewNode
        self.length += 1
        return True

    # TO remove from a particular index
    def Remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.PopFirstNode(value)
        if index == self.length:
            return self.PopNode(value)
        current = self.GetByIndex(index - 1)
        after = current.next
        current.next = after.next
        after.next = None
        self.length -= 1
        return None

    def Reverse(self):
        if self.length == 0 or self.length == 1:
            return None
        current = self.head
        self.head = self.tail
        self.tail = current
        after = None
        before = None
        while current:
            after=current.next
            current.next=before
            before=current
            current=after
        return True


new_list = LinkedList(5)
new_list.AddNode(8)
new_list.AddNode(9)
new_list.AddNode(4)
# new_list.PopNode()
new_list.PrependNode(23)
# new_list.PopFirstNode()
# print((new_list.GetByIndex(3)).value)           # (.value) is used here because here the object will get returned which will have a reference to the next
# new_list.SetValueByIndex(356,3)
# new_list.Insert(5,335)
# new_list.Remove(4)
print(new_list.Reverse())
new_list.Display()
