list1=['a','b','c','d','e','f','g','h']


def insertShiftArray(arr,value):
  new_list=[]
  for a in arr:
    if arr.index(a) == len(arr)//2 :
      new_list.append(value)
    else:
      new_list.append(a)
  return new_list   

print(insertShiftArray(list1,'z'))






def removeMiddleValue(arr):
  new_list=[]
  for a in arr:
    if arr.index(a) == len(arr)//2 :
      continue
    else:
      new_list.append(a)
  return new_list   

print(removeMiddleValue(list1))