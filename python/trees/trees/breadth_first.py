def breadth_first(tree_):
    breadth = []
    breadth+=tree_.root
    list_of_items = []

    while breadth[0]:
      front = breadth[0]
      for i in breadth:
        arr=[]
        if i==front:
          continue
        arr+=i
        breadth=arr

      list_of_items += [front.data]

      if front.left:
        breadth+=[front.left]

      if front.right:
        breadth+=[front.right]

    return list_of_items
