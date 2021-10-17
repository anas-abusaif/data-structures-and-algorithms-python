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

    def __str__(self):
        result = ""
        while self.head is not None:
            result += "{ " + str(self.head.data_) + " } -> "
            self.head = self.head.next_
        result += "NULL"
        return result
    def append(self, value):
        """
        Adds a node with a value to the end of tje list
        """
        node_ = Node(value)
        if not self.head:
            self.head = node_
        else:
            current = self.head
            while current.next_ is not None:
                current = current.next_
            current.next_ = node_

    def insertBefore(self,value, new_value):
        """
        takes two arguments to add a node 
        of a new_value before node has value==value in the List
        """
        try:
            node_ = Node(new_value)
            current = self.head
            if(current.data_ == value):
                self.insert(new_value)
                return
            while(current.next_.data_ != value):
                current = current.next_
            a = current.next_
            current.next_=node_
            node_.next_ = a
        except TypeError:
            return f'please enter a proper type'
        except:
            return "No change, method exception"

    def insertAfter(self,value, new_value):
        """
        method takes two arguments to add a node 
        of a new_value after node has value==value in Linked List
        """
        try:
            node = Node(new_value)
            current = self.head
            while(True):
                if(current.data_ == value):
                    a = current.next_
                    current.next_ = node
                    node.next_ = a
                    break
                current = current.next_
        except:
            return "No change, method exception"