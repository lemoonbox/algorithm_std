#1. linked list 생성기
#2. link 삽입기 원하는 데이터와 index 순서를 입력하면 삽입


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def create_list(self, datalist):
        now_node = Node(datalist[0])
        self.head= now_node
        for i in range(1, len(datalist)):
            new_node = Node(datalist[i])
            now_node.next = new_node
            now_node = new_node

    def prt_allnode(self):
        now_node = self.head
        while 1:
            print("",now_node.data, end="")
            if now_node.next == None: break
            now_node = now_node.next

    def insertnode(self, data, index =0):
        new_node = Node(data)
        now_node = self.head

        if index == 0:
            self.head = new_node
            self.head.next = now_node
            return

        for i in range(0, index-2):
            now_node = now_node.next

        new_node.next = now_node.next
        now_node.next = new_node



linklist = LinkedList()
linklist.create_list([1,2,3,4,5])
linklist.prt_allnode()


linklist.insertnode(10, 6)
linklist.prt_allnode()