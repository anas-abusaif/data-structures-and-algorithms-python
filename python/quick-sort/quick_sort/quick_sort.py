
def quick_sort(arr,left,right):
  if type(arr) is not list:
    return 'input is not a list'
  if left<right:
    postion = partition(arr,left,right)
    quick_sort(arr,left,postion-1)
    quick_sort(arr,postion+1,right)
    return arr

def partition(arr,left,right):
  pivot=arr[right]
  low=left-1
  for i in range(left,right):
    if arr[i] <= pivot:
      low=low+1
      swap(arr,i,low)
  swap(arr, right, low + 1)
  return low + 1

def swap(arr,i,low):
  temp=arr[i]
  arr[i]=arr[low]
  arr[low]=temp


