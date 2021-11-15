class Node:
    """
     A class for creating a node

    data: any
    next: Node
    """

    def __init__(self, data_, next_=None):
        self.data_ = data_
        self.next_ = next_


class Linked_list:
    """
    A class for creating instances of a Linked List.

    Data and other attributes defined here:

    head: Node | None

    Methods defined here

    insert(value: any)
    contains(value: any) -> bool
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """
        Arguments: value
        Returns: nothing
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        """
        self.head = Node(value, self.head)

    def includes(self, value):
        """
        Arguments: value
        Returns: Boolean
        Indicates whether that value exists as a Node’s value somewhere within the list.

        """
        if self.head == None:
            return False
        else:
            this_node = self.head
            while self.head:
                if this_node.data_ == value:
                    return True
                this_node = this_node.next
                return False

    def __str__(self):
        """
        to string
        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        result = ""
        this_node = self.head
        while this_node:
            result += "{ " + str(this_node.data_) + " } -> "
            this_node = this_node.next_
        result += "NULL"
        return result

    def append(self, value):
        """
        Adds a node with a value to the end of the list
        """
        node_ = Node(value)
        if not self.head:
            self.head = node_
        else:
            current = self.head
            while current.next_:
                current = current.next_
            current.next_ = node_

    def insertBefore(self, value, new_value):
        """
        takes two arguments to add a node
        of a new_value before node has value==value in the List
        """
        try:
            node_ = Node(new_value)
            current = self.head
            if current.data_ == value:
                self.insert(new_value)
                return
            while current.next_.data_ != value:
                current = current.next_
            a = current.next_
            current.next_ = node_
            node_.next_ = a
        except IndexError:
            return "please enter a proper type"
        except:
            return "No change, method exception"

    def insertAfter(self, value, new_value):
        """
        method takes two arguments to add a node
        of a new_value after node has value==value in Linked List
        """
        try:
            node = Node(new_value)
            current = self.head
            while True:
                if current.data_ == value:
                    a = current.next_
                    current.next_ = node
                    node.next_ = a
                    break
                current = current.next_
        except:
            return "No change, method exception"

    def return_Kth_value(self, k):
        """
        takes one integer and reterns the value of the integers position from the tail
        """
        try:
            current = self.head
            list_values = []
            while current.next_:
                list_values.append(current.data_)
                current = current.next_
            list_values.append(current.data_)
            list_values.reverse()
            return list_values[k]
        except IndexError:
            return "such value does not exist"

    def zipLists(self, list1, list2):
        """
        Arguments: 2 linked lists
        Return: the two lists zipped into one list
        """
        current1 = list1.head
        current2 = list2.head
        list3 = Linked_list()

        while True:
            if current1.next_:
                list3.append(current1.data_)
            elif current2.next_:
                list3.append(current2.data_)
                current2 = current2.next_
            current1 = current1.next_
            if current2.next_:
                list3.append(current2.data_)
            elif current1.next_:
                list3.append(current1.data_)
                current1 = current1.next_
            current2 = current2.next_
            if current2.next_ == None and current1.next_ == None:
                break
        return list3.__str__()

