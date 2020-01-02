def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

l=[10,90,21,1,2,34,56]
s=['sai','aditya','ede','a','abc','zoo','az','boo']
bubble_sort(l)
bubble_sort(s)
print(l)
print(s)
