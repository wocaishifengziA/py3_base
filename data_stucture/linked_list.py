class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self._head

            while pos > 1:
                cur = cur.next
                pos -= 1
            cur_next = cur.next
            cur.next = node
            node.next = cur_next

    def remove(self, item):
        """删除元素"""
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """搜索元素"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    linked = SingleLinkList()
    linked.append("a")
    linked.append("b")
    linked.append("c")

    # linked.travel()
    linked.insert(4, "x")
    linked.travel()





