def insetion_sorting(arr):
  if type(arr) is not list:
    return 'input is not a list'
  for i in range(len(arr)):

    j=i-1
    temp=arr[i]

    while j >= 0 and temp < arr[j]:

      arr[j + 1] = arr[j]
      j = j - 1

    arr[j + 1]=temp
  return arr
