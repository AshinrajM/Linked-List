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

    def CheckPalindrome(self):
        if self.length == 0 or self.length == 1:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = None
        current = slow.next

        while current is not None:
            after = current.next
            current.next = second
            second = current
            current = after

        first_half = self.head
        second_half = second

        while second_half is not None:
            if first_half.value != second_half.value:
                return "Not palindrome"
            first_half = first_half.next
            second_half = second_half.next
        return "Palindrome"


abc = Latest(5)
abc.Append(4)
abc.Append(3)
abc.Append(4)
abc.Append(5)
print(abc.CheckPalindrome())
