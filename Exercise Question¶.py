#!/usr/bin/env python
# coding: utf-8

# # Exercise Question

# # Rungsiman laokasetwit

# # 6310301029

# 
# # Exercise Question 1 : Given a two list. Create a third list by picking an odd-index element from the first list and even index element from second.

# In[2]:


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3,list3_1,list3_2  = [],[],[]

print("Element at odd-index positions from list 1")
for i in range(1,len(list1)):
    if i % 2 == 0 :
        list3_1.append(list1[i-1])
print(list3_1)

print("Element at even-index position from list 2")
for i in range(1,len(list2)+1):
    if i % 2 != 0 :
        list3_2.append(list2[i-1])
print(list3_2)

print("Printing final third list")
list3 = [i for i in list3_1]
list3 += [i for i in list3_2]
print(list3)


# # Exercies Question 2 : given an input list removes the element at index 4 and add it to the 2nd position and also ,at the end of the list

# In[4]:


List1  = [34,54,67,89,11,43,94]
print("Original list",List1)

tmp = List1[4]
List1.remove(tmp)
print('List After removing element at index 4 ',List1)
List1.insert(2,tmp)
print('List After Adding element at index 2',List1)
List1.append(tmp)
print("List after Adding element at list",List1)


# # Exercise Question 3 : Given a list slice It into a 3 equal chunks and reverse each list

# In[5]:


EX_List = [11,45,8,23,14,12,78,45,89]
print("Original list",EX_List)
i,n,tmp = 1,2,[]
while EX_List != []:
    tmp = EX_List[:3]
    EX_List = EX_List[n+1:]
    print('Chunk',i,tmp)
    tmp.reverse()
    print('After reversing it',tmp)
    i += 1


# # Exercise Question 4 : Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

# In[6]:


List = [11,45,8,11,23,45,23,45,89]
print("Original list",List)
dis = {}
while List != []:
    count = [i for i in List if i == List[0]]
    dis.update({List[0]:len(count)})
    tmp = List[0]
    for i in range(len(count)) :
        List.remove(tmp)
        
print("Printing count of each item",dis)


# # Exercise Question 5 : Given a list of equal size create a set such that it shows the element from both the first set
# 

# In[8]:


one = [2,3,4,5,6,7,8]
second = [4,9,16,25,36,49,64]
result = set()
for i in one :
    if (i*i) in second :
        result.add(tuple([i,second[second.index(i*i)]]))
print("one List",one)
print("second",second)
print("Result is",result)


# # Exercise Question 6 : Given a following two sets find the intersection and remove those elements from the first set¶
# 

# In[9]:


firstSet = {65,42,78,83,23,57,29}
Second = {67,73,43,48,83,57,29}
tmp = set()
print("First Set : ",end="")
for i in firstSet :
    print(i,end=" ")

print("\nSecond Set : ",end="")
for i in Second :
    print(i,end=" ")
    
print("\nIntersection is  : ",end="")
for i in  firstSet :
    if i in Second :
        print(i,end=" ")
    else:
        tmp.add(i)

print("\nFirst Set after removing common element : ",end="")
for i in tmp :
    print(i,end=" ")


# # Exercise Question 7 : Given two sets,Checks if One Set is Subset or superset or superset of Another Set .if the subset is found delete all element from that set

# In[10]:


frist = {57,83,29}
seccond = {67,73,43,48,83,57,29}

print("\nFirst Set ",end=" ")
for i in frist :
    print(i,end=" ")
    
print("\nSecond Set ",end=" ")
for i in seccond :
    print(i,end=" ")
    
print("\n\nFirst set is subset of second set - ",frist.issubset(seccond))
print("second set is subset of first set - ",seccond.issubset(frist))
print("\n\nFirst set is subset of second set - ",frist.issuperset(seccond))
print("second set is subset of first set - ",seccond.issuperset(frist))

print("\n\nFirst Set ",set())
print("Second Set ",end=" ")
for i in seccond :
    print(i,end=" ")


# # Excercise Qquestion 8 : Iterate a given list and Check if a given elemant already in a dictionary as a key's value if not delete it from the list

# In[11]:


rollNumber = [47,64,69,39,76,83,95,97]
sampleDict = {'jhon':47,'Emma':69,'Kelly':76,'Kason':97}
print("Given: ")
print('rollNumber = ',rollNumber)
print('sampleDict = ',sampleDict)
print("\nExpected Outcome:")
tmp = sampleDict.values()
tmp2 = [47,64,69,39,76,83,95,97]
for i in range(len(tmp2)) :
    if tmp2[i] not in tmp :
        rollNumber.remove(tmp2[i])
print('after removing unwanted element from list  ',rollNumber)


# # Exercise Question 9 : Given a dictionary get all values from the dictionary and add it in a list but don't add duplicates¶
# 

# In[12]:


speed = {'jan':47,'feb':52,'march':47,'April':44,'May':52,'June':53,'july':54,'Aug':44,'Sept':54}
values_new = speed.values()
tmp = []
for i in values_new :
    if i not in tmp :
        tmp.append(i)
tmp


# # Exercise Question 10 : Remove duplicate from a list and create a tuple and find the minimum and maximum number¶
# 

# In[18]:


sample = [87,45,41,65,94,41,99,94]
print("For Example :")
print("sampleList = ",sample)
tmp = []
for i in sample :
    if i not in tmp :
        tmp.append(i)
sample = tmp
print("Expected Outcome :")
print("unique items = ",sample)
print("tuple = ",tuple(sample))
print("min : ",min(sample),"max :" ,max(sample))

