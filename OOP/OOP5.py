# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, item):
#         node = Node(item)
#         if self.head is None:
#             self.head = node  # 为空，就增加一个node
#         else:
#             p = self.head  # 假设一个指针，从头开始
#             while p.next is not None:  # 如果next=None,就增加一个node
#                 p = p.next
#             p.next = node
#
#     def iter_nodes(self):
#         p = self.head  # 指针从头开始，不为None就打印
#         while p is not None:
#             yield p.data
#             p = p.next
#
#
# if __name__ == '__main__':
#     link = LinkedList()
#     for x in range(5):
#         link.append(x)
#     print(list(link.iter_nodes()))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.pre = None
#         self.next = None
#
#
# class DLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, item):
#         node = Node(item)
#         if self.head is None:
#             self.head = node
#         else:
#             p = self.head  # p=0
#             while p.next is not None:  # p.next=1
#                 p = p.next  # p=1
#             p.next = node
#             p.pre = p
#
#     def iter_nodes(self):
#         p = self.head
#         while p is not None:
#             yield p.data
#             p = p.next
#
#     def pop(self):
#         pre = None
#         p = self.head  # p=0
#         while p.next is not None:  # p.next = 1
#             pre = p  # p=0
#             p = p.next  # p=1
#         pd = pre.next
#         pre.next = None
#         return pd.data
#
#     def length(self):
#         p = self.head
#         i = 0
#         while p is not None:  # p=0
#             i += 1
#             p = p.next
#         return i
#
#     def insert(self, position: int, item):
#         if position < 0:
#             return 'index error'
#         elif position > self.length() - 1:
#             self.append(item)
#         else:
#             node = Node(item)
#             p = self.head
#             i = 1
#             while p is not None:  # p=0
#                 p = p.next  # p=1
#                 if i == position:  # i=1
#                     node.pre = p.pre.pre
#                     node.next = p
#                     p.pre = node
#                     p.pre.next = node
#
#                     break
#                 i += 1
#
#     def remove(self):
#         pass
#
#
# if __name__ == '__main__':
#     link = DLinkedList()
#     for x in range(10, 15):
#         link.append(x)
#     print(list(link.iter_nodes()))
#     print(link.length())
#     print(link.pop())
#     print(list(link.iter_nodes()))
#     print(link.length())
#     link.insert(2, 2)
#     print(list(link.iter_nodes()))
#     print(link.length())


# 双向链表
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#     def __repr__(self):
#         return '{}'.format(self.item)
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.__size = 0
#
#     def __len__(self):
#         return self.__size
#
#     def append(self, item):
#         node = Node(item)
#         if self.head is None:  # 为空
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node  # 链表的尾巴的下一个是node
#             node.prev = self.tail  # node的前一个是链表的尾巴
#             self.tail = node  # 新的尾巴是node
#             self.__size += 1
#         return self
#
#     def pop(self):
#         if self.head is None:  # 为空
#             raise Exception('Empty')
#         else:  # 不为空
#             node = self.tail  # 链表的尾部
#             item = node.item  # 链表尾部的值
#             prev = node.prev  # 链表尾部的前一个
#             if prev is None:  # 链表只有一个
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.tail = prev  # 当前的尾巴是原尾巴的前一个
#                 prev.next = None  # 原尾巴的前一个的下一个为None
#             self.__size -= 1
#             return item
#
#     def iternodes(self, reverse=False):
#         current = self.head if not reverse else self.tail
#         while current:
#             yield current
#             current = current.next if not reverse else current.prev
#
#     def insert(self, index, item):
#         if index < 0:
#             raise IndexError
#         current = None
#         for i, nodes in enumerate(self.iternodes()):
#             if i == index:
#                 current = nodes
#                 break
#         else:  # 没有break，没有找到等于index的索引，说明超界了，尾部追加
#             self.append(item)
#             return
#
#         node = Node(item)
#         prev = current.prev
#         next = current
#         if prev is None:  # index为0时
#             self.head = node
#             node.next = next
#             next.prev = node
#         else:
#             next.prev = node
#             prev.next = node
#             node.prev = prev
#             node.next = next
#         self.__size += 1
#
#     def remove(self, index):
#         if self.tail is None:
#             raise Exception('Empty')
#         if index < 0:
#             raise IndexError
#         current = None
#         for i, nodes in enumerate(self.iternodes()):
#             if i == index:
#                 current = nodes
#                 break
#         else:  # 没有break，没有找到等于index的索引，说明超界了
#             raise IndexError
#
#         prev = current.prev
#         next = current.next
#         # 有四种情况
#         if prev is None and next is None:  # 只有一个时
#             self.head = None
#             self.tail = None
#         elif prev is None:  # index = 0时
#             self.head = next
#             next.prev = None
#         elif next is None:  # index是最后一个
#             self.tail = prev
#             prev.next = None
#         else:  # 在中间位置
#             prev.next = next
#             next.prev = prev
#         del current
#         self.__size -= 1
#
#     __iter__ = iternodes
#
#     def __getitem__(self, index):
#         start = 0 if index > 0 else 1
#         reverse = False if index > 0 else True
#         for i, node in enumerate(self.iternodes(reverse), start):
#             if i == abs(index):
#                 return node
#         else:
#             raise IndexError
#
#     def __setitem__(self, index, value):
#         self[index].item = value
#         # self.[index]触发__getitem__,node.item = value
#
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# for i in ll:
#     print(i)
# ll[1] = 5
# print(ll[1])


class Property:

    def __init__(self, fn):  # data=Property(fn)
        self.fn = fn
        self.fn_s = None

    def __get__(self, instance, owner):  # instance = A(5),owner=A
        if instance is not None:
            return self.fn(instance)

    def __set__(self, instance, value):
        if callable(self.fn_s):
            self.fn_s(instance, value)
        else:
            raise AttributeError('{} can not assign'.format(self.fn_s.__name__))

    def setter(self, fn):  # self = Property(data)
        self.fn_s = fn  # 这是为实例增加属性，对应一个函数，不会绑定
        return self


class A:
    def __init__(self, data):
        self._data = data

    @Property  # data = Property(data);data = data.getter(data)
    def data(self):  # data是Property的实例，然后data被返回的值覆盖
        return self._data

    @data.setter  # data = data.setter(data)
    def data(self, value):
        self._data = value


a = A(5)
print(a.data)
a.data = 10
print(a.data)

























































































