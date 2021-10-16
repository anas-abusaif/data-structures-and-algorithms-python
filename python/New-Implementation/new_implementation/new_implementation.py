class Node:
    def __init__(self, data_, next_=None):
        self.data_ = data_
        self.next_ = next_


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        if self.head == None:
            return False
        else:
            while self.head is not None:
                if self.head.data_ == value:
                    return True
                self.head = self.head.next
                return False

    def to_string(self):
        result = ""
        while self.head is not None:
            result += "{ " + str(self.head.data_) + " } -> "
            self.head = self.head.next_
        result += "NULL"
        return result
