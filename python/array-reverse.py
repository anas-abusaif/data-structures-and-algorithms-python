nums=[1,2,3,4,5,6,7,8,9]


def array_reverse(list):
 x=len(list)-1
 new_list=[]
 for l in list:
   new_list.append(list[x])
   x-=1
 return new_list

print(array_reverse(nums))
