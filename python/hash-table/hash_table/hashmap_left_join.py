def left_join(table1, table2):
    output = []
    for item in table1._HashTable__buckets:
        if item :
            current = item.head
            left_join = []
            while current:
                left_join.append(current.value[0])
                left_join.append(current.value[1])
                if table2.contains(current.value[0]):
                    left_join.append(table2.get(current.value[0]))
                else:
                    left_join.append(None)

                current = current.next

            output.append(left_join)
    return output