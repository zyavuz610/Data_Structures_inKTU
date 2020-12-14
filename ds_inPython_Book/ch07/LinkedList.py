class LinkedList:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    def __init__(self, e, prev, next):                  # initialize node's fields
      self._element = e                                 # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._head = None
    self._tail = None
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0


  def add_first(self,e):
    newest = self._Node(e,None,self._head)
    if self._size == 0:       # liste boş ise
       self._head = newest
       self._tail = newest
    else:                     # dolu listenin başına eleman ekle
        self._head._prev = newest
        self._head = newest
    self._size += 1

  def add_last(self,e):
    newest = self._Node(e,self._tail,None)
    self._tail._next = newest
    self._tail = newest
    self._size += 1

  def insert(self,e):
    if self._head == None or e < self._head._element:          # if list is empty
      self.add_first(e)
    elif e > self._tail._element:   # add last
      self.add_last(e)
    else:                           # insert between
      cur = self._head
      while cur._next != None and e > cur._element :
        cur = cur._next
      newest = self._Node(e,cur._prev,cur)
      cur._prev._next = newest
      cur._prev = newest
      self._size += 1

  def print_list(self):
    cur = self._head
    while cur != None:
      print(cur._element," ",end="")
      cur = cur._next
    print("")

  def print_list_reverse(self):
    cur = self._tail
    while cur != None:
      print(cur._element," ",end="")
      cur = cur._prev
    print("")
  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element