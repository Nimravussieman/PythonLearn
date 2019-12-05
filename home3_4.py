class Node:
    def __init__(self,initdata):
       self.data = initdata
       self.next = None

    def getData(self):
       return self.data

    def getNext(self):
       return self.next

    def setData(self,newdata):
       self.data = newdata

    def setNext(self,newnext):
       self.next = newnext

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
       self.head = None

    def isEmpty(self):
       return self.head == None

    def add(self,item):
       temp = Node(item)
       temp.setNext(self.head)
       self.head = temp

    def sddSorted(self,item):
        temp = Node(item)
        current = self.head
        prev = None
        while current:
            if current.getData() > item:
                break
            prev = current
            current = current.next

        if prev:
            self.dda(prev,item)
        elif current:
            self.dda(current, item)
        else:
            self.add(item)


    def dda(self,node,item):
        newItem = Node(item)
        newItem.setNext(node.next)
        node.next = newItem


    def size(self):
       current = self.head
       count = 0
       while current != None:
           count = count + 1
           current = current.getNext()
       return count

    def serch(self,item):
       current = self.head
       while current:
            if current.getData() == item:
                return current
            else:
                current = current.getNext()
       else:
           return None

    def dell(self,item):
        current = self.head
        prev = None
        while current != None:
            if current.getData() == item:
                if prev:
                    prev.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                break
            else:
                prev = current
                current = current.getNext()

    def pop(self,index=-1):
        count = self.size()
        if index < 0:
            index = count + index
        if index > self.size()-1 and index < 0:
            return None


        try:
            i = 0
            current = self.head
            prev = None
            while current:
                if i == index:
                    break
                i += 1
                prev = current
                current = current.getNext()
            if prev:
                prev.setNext(current.getNext())
            # elif not prev and not count:
            #     self.head = current.getNext()
            else:
                self.head = current.getNext()

            return current


        except:
            return None


# linc = LinkedList()
# linc.add(1)
# linc.add(2)
# linc.add(3)
# linc.add(4)
# print((linc.pop()))
# print(linc.serch((1)))
# print((linc.pop(0)))
# print(linc.serch((4)))
# print(linc.size())
# print(linc.serch((2)))
# print(linc.serch((3)))


# print(linc.serch((2)))
# linc.dell(2)
# node = linc.serch((1))
# print(linc.head == node)


class Node:
    def __init__(self,next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def getData(self):
       return self.data

    def getNext(self):
       return self.next

    def getPrev(self):
        return self.prev

    def setPrev(self, new_prev):
        self.prev = new_prev

    def setData(self,newdata):
       self.data = newdata

    def setNext(self,newnext):
       self.next = newnext

    def __str__(self):
        return str(self.data)


class LinkedList2:

    def __init__(self):
       self.head = None

    def isEmpty(self):
       return self.head == None

    def add(self,item):
       temp = Node(item)
       temp.setNext(self.head)
       self.head.prev = temp
       self.head = temp

    def addBack(self,item):
        newNode = Node(item)
        curent = self.head
        while curent.next:
            curent = curent.next
        else:
            newNode.prev = curent
            curent.next = newNode

    def insert(self,item):
        curent = self.serch(item)
        if curent:
            newNode = Node(item)
            newNode.next = curent.next
            newNode.prev = curent
            curent.prev = newNode
        else:
            self.addBack(item)


    def size(self):
       current = self.head
       count = 0
       while current != None:
           count = count + 1
           current = current.getNext()
       return count

    def serch(self,item):
       current = self.head
       while current:
            if current.getData() == item:
                return current
            else:
                current = current.getNext()
       else:
           return None

    def dell(self,item):
        current = self.head
        prev = None
        while current != None:
            if current.getData() == item:
                if prev:
                    prev.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                break
            else:
                prev = current
                current = current.getNext()


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def __len__(self):
        return len(self.items)



def func1(stringi):
    stack = Stack()
    resStr = ''
    oper = {'+':1,'*':2}
    for x in stringi:
        if x not in oper.keys():
            resStr += x
        elif stack.is_empty():# or stack.peek() == oper[2]:
            stack.push(x)
        elif oper[x] > oper[stack.peek()]:
            stack.push(x)
        else:
            while oper[stack.peek()] >= oper[x]:
                resStr += stack.pop()
    while not stack.is_empty():
        resStr += stack.pop()
    return resStr
# print(func1("a+b*c"))


class Queue:
   def __init__(self):
       self.items = LinkedList()

   def is_empty(self):
       return self.items == []

   def push(self, item):
       self.items.add(item)#.insert(0,item)

   def pop(self):
       return self.items.pop()

   def __len__(self):
       return self.items.size()



class Node:
   def __init__(self, data):
       self.left = None
       self.right = None
       self.data = data

   def __str__(self):
       return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val, node=None):
        if self.root == None:
            self.root = Node(val)
        else:
            if not node:
                node = self.root
            if val < node.data:
                if node.left != None:
                    self.add(val, node.left)
                else:
                    node.left = Node(val)
            else:
                if node.right != None:
                    self.add(val, node.right)
                else:
                    node.right = Node(val)

    def finde(self,item):
        current = self.getRoot()
        while current:
            if current.data == item:
                return current.data
            elif current.data > item:
                current = current.left
                continue
            else:
                current = current.right
                continue
        return None

def show(node,s):

    if node.left:
        show(node.left,'\t{}'.format(s))

    print(s,node.__str__())

    if node.right:
        show(node.right,'\t{}'.format(s))


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
show(tree.getRoot(),'')
print(tree.finde(1))
print(tree.finde(8))























# def show5(node,s):
#     string=''
#     if node.left:
#         show5(node.left,' {}'.format(s))
#
#     print(node.__str__() + s + '\n')
#
#     if node.right:
#         show5(node.right,' {}'.format(s))

