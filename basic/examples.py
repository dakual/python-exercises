liste = []
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]
list3 = [[1,2,3,4],[5,6,7],[8,9,10,11],[12,13,14,15,16],[17,18,19],[20]]

liste = [i*i for i in list1 if i not in list2]

liste = [k for i in list3 for k in i]


methods = []
for method in dir(list):
    if not method.startswith("__"):
        methods.append(method)
#print(methods)

liste = [method for method in dir(list) if not method.startswith("__")]
#print(liste)


def topla(*args):
    toplam = 0
    for x in args:
        toplam += x
    
    return toplam

list5 = set(map(lambda x,y : x + y, list1, list2))
print(list5)


def negativenumbers(a,b):
  # Checking condition for negative numbers
  # single line solution
  out=[i for i in range(a,b+1) if i<0]
  # print the all negative numbers
  print(*out)
 
# driver code
# a -> start range
a=-4
# b -> end range
b=5
negativenumbers(a,b)