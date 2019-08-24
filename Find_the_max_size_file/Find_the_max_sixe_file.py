#!/usr/bin/env python
# coding: utf-8

# In[2]:



import os
print("Program to find the file with maximum size inside a directory")
def fn():
    path=input("Enter the path: ")
    # path=os.getcwd()
    # print(path)
    # path=os.path.join(path,"Desktop","udemy-dl-master","test_pyhton")
    # path=os.path.join(path,"Desktop","udemy-dl-master")
    # path=os.path.join(path,"Desktop")
    print(path)

    max_size=-1;
    for root,dirs,name in os.walk(path):
    #     print("Hello")
    #     print(root)
    #     print(dirs)
    #     print(name)
        for i in name:
    #         print(os.path.join(root,i))
    #         print(os.path.join(root,i))
            size = os.path.getsize(os.path.join(root,i))
    #         print(i,size)
            if(size>max_size):
                path_max=os.path.join(root,i)
                name_max=i
                max_size=size
    print("\n")
    print("File  with maximum size :- ")
    print("Path:- ",path_max)
    print("Name:- ",name_max)
    if(max_size<1000):
        print("Size:- ",max_size,"bytes")
    elif(max_size<1000000):
        print("Size:- ",int(max_size/1000),"KB")
    elif(max_size<1000000000):
        print("Size:- ",int(max_size/1000000),"MB")
    else:
        print("Size:- ",int(max_size/1000000000),"GB")
    
    o=input("Do you want to continue?(y\\n)")
    return o
while(fn()=='y'):   
    print("\n\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




