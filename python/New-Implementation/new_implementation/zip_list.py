from new_implementation.new_implementation import Linked_list

def zipLists(self,list1,list2):
        '''
        Arguments: 2 linked lists
        Return: the two lists zipped into one list
        '''
        current1=list1.head
        current2=list2.head
        list3=Linked_list()

        while True:
            if current1.next_:
                list3.append(current1.data_)
            elif current2.next_:
                list3.append(current2.data_)
                current2=current2.next_
            current1=current1.next_
            if current2.next_:
              list3.append(current2.data_)
            elif current1.next_:
                list3.append(current1.data_)
                current1=current1.next_
            current2=current2.next_
            if current2.next_==None and current1.next_==None:
                break
        return list3.__str__()