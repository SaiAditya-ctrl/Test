f=open("data.txt",'w')
f.write("hello sai aditya how are you ")
f.close()
s=open("data.txt",'r')
contents=s.read()
print(contents)
f.close()
l=[]
l=contents.split(" ")
l.pop()
l.append("!")
print(l)
p=[]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    
    def __init__(self):
        self.head=None
    def print_list(self):
        tem=self.head
        while(tem):
            print(tem.data)
            
            tem=tem.next


    def adding(self):
    
        self.llist=LinkedList()
        self.llist.head=Node(l[0])
        self.temp=self.llist.head
        
        for i in range(1,len(l)):
                    
                   self.temp.next=Node(l[i])
                   self.temp=self.temp.next
       
        self.llist.print_list()
l2=LinkedList()
l2.adding()
x=input('enter the element to be searched ')
if(x in l):
    print('found at index',l.index(x))
    l.remove(x)
    l2.adding()
else:
    print('not found')
    l.append(x)
    l2.adding()
l2.print_list()
string=' '
string=string.join(l)
print(string)
a=open("data.txt",'w')
for i in string:
    a.write(i)
a.close()
b=open("data.txt",'r')
cont=b.read()
b.close()
print(cont)


