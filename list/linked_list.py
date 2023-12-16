#linked_list.py
#
# Author: Josiah Lam
# Email: j23lam@uwaterloo.ca
# Student ID: 21026577
#
# Source code for the LinkedList and ListNode class

class ListNode:
  """A node in a linked list"""

  def __init__(self, data, next=None):
    """Constructor"""
    self.data = data
    self.next = next
    
    #NOTE principles of linked data structure
    #point node -- means point at the node
    #point node.next -- means point at the node's direction 


class LinkedList:
  """ LinkedList
    A simplified List implemented using linked nodes.
    Uses explicit "get" and "set" functions rather
    than sequence indexing notation.
  """

  def __init__(self):
    """Create an empty list."""
    self._length = 0
    self._front = None #this is my first node
    

  ###################
	#    Accessors    #
	###################

  def length(self) -> int:
    """Return number of elements stored in the array."""
    return self._length
  
  def contains(self, value, map_to_key=lambda x : x) -> bool:
    """ contains
      Returns True if value is in the list, False otherwise
      
      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    return self.find_index_byvalue(value, map_to_key=map_to_key) >= 0



  def find_index_byvalue(self, value, map_to_key=lambda x : x) -> int:
    """ find_index_byvalue
      Returns the first index of value, or -1 if not found
      
      value: the value to find as an object,
        or the key to compare to (if using map_to_key)

      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    for i in range(self.length()):
      if map_to_key(self.get(i)) == value:
        return i
    return -1
  
  
  def get(self, k : int) -> object:
    """Return element at index k."""
    if k < 0 or k >= self._length:
      raise IndexError('invalid index')

    return self._get_node_k(k)
    

  ##################
	#    Mutators    #
	##################

  def _get_node_k(self, k):
    """ Optional private helper function """
    
    #set varaibles
    cur = self._front
    count = 0
    
    #loop to index k 
    while count != k:
      count += 1
      cur = cur.next
    
    #return data at index index k
    return cur.data

  def set(self, k, value):
    """Set element at index k"""
    
    #set varaibles
    cur = self._front
    count = 0
    
    #if input index k less than 0 or greater than or equal to the length of linked list -- raise IndexError
    if k < 0 or k >= self._length:
      raise IndexError("invalid index")
    
    #if empty linkedlist
    elif self._length == 0:
      #set front.data to the input value
      self._front.data = value
    
    #if not empty linkedlist
    else: 
      #loop to index k
      while count < k:
        cur = cur.next
        count += 1
      
      #set the input value to .data at index k
      cur.data = value



  def append(self, obj):
    """Add object to end of the array."""
    
    #set varaibles
    cur = self._front
    new_node = ListNode(obj)
    
    #if empty linked list
    if cur == None:
      #point cur to obj
      self._front = new_node
      #add 1 to linkedlist length
      self._length += 1

    #not empty linked list
    else:
      #loop until the end of the linkedlist -- check for null pointers
      while cur.next != None:
        cur = cur.next
       
      #point cur.next to the new node
      cur.next = new_node
      #add 1 to linkedlist length
      self._length += 1




  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""

    #set varaibles
    cur = self._front
    count = 0
    new_node = ListNode(value)

    #if input index k less than 0 or greater than or equal to the length of linked list -- raise IndexError
    if k < 0 or k > self._length:
      raise IndexError("Please enter a index k within the range")
    
    #inserting to index 0
    elif k == 0:
      #point new_node.next to the front
      new_node.next = self._front
      
      #point front to new_node
      self._front = new_node
      
      #add 1 to linkedlist length
      self._length += 1
      
    #inserting to last index 
    elif k == self._length:
      #call append function
      self.append(value)
    
    #inserting to index k (not front and not back)  
    else:
      #loop to index k - 1 (since we need to insert at index k, therefore, it is better not to operate action on index k for a linkedlist)
      while count < k -1:
        count += 1
        cur = cur.next
      
      #point cur.next to new_node, since looping till insert index k - 1 (the node before the oringal insert node)
      
      #point new_node.next (new_node direction) to cur.next (cur's direction), which cur.next points to the rest of the linkedlist
      new_node.next = cur.next
      
      #point the cur.next (cur's direction) to the new_node
      cur.next = new_node
      
      #add 1 to linkedlist length
      self._length += 1

    

  def remove(self, k : int) -> object:
    """Remove the value at index k, returning it"""

    #set variables
    cur = self._front
    count = 0

    #if input index k less than 0 or greater than or equal to the length of linked list -- raise IndexError    
    if k < 0 or k >= self._length:
      raise IndexError("Please enter a index k within the range")
    
    #if removing first node
    elif k == 0:
      #a temporary pointer to front.data (first node's data)
      tmp = self._front.data
      
      #point the front to front.next (skips front.data)
      self._front = self._front.next
      
      #minus 1 to linkedlist length
      self._length -= 1
      
      #retrun temporary node
      return tmp
    
    #if removing node in the list
    else: 
      #loop to index k - 1 (since we need to remove index k, therefore, it is better not to operate action on index k for a linkedlist)
      while count < k - 1:
        cur = cur.next
        count += 1
      
      #a temporary pointer to the cur.data (index k node's data )
      tmp = cur.next.data
      
      #point the cur.next (cur's direction) to cur.next.next (two node after cur) -- (skip index k .data)
      cur.next = cur.next.next
      
      #minus 1 to linkedlist length
      self._length -= 1
      
      #return temporary node
      return tmp


	#################
	#    Sorting    #
	#################

  def _swap(self, i : int, j : int):
    """_swap
      Optional private helper function to swap two objects in place.
      Intended to help with sorting algorithms
    """
    # check if both indices are within range
    # if not 0 <= i < self._length:
    #   raise IndexError("i is out of index range")
    # if not 0 <= j < self._length:
    #   raise IndexError("j is out of index range")
    
    # #case I -- swap front and back node 
    # if i == 0 and j == self._length:
    #   temp_front = self.remove(0)
    #   temp_back = self.remove(j)
    #   self.insert(0, temp_back)
    #   self.insert(j, temp_front)
      
    # #case II -- swap front and middle node
    # elif i == 0 and j != self._length:
    #   temp_front = self.remove(0)
    #   temp_middle = self.remove(j)
    #   self.insert(0, temp_middle)
    #   self.insert(j, temp_front)

    # #case III -- swap middle and middle node
    # elif i != 0 and j != self._length:
    #   temp_middle1 = self.remove(i)
    #   temp_middle2 = self.remove(j)
    #   self.insert(i, temp_middle2)
    #   self.insert(j, temp_middle1)

    # #case IV -- swap middle and back node
    # elif i != 0 and j == self._length:
    #   temp_middle = self.remove(i)
    #   temp_back = self.remove(j)
    #   self.insert(i, temp_back)
    #   self.insert(j, temp_middle)
    pass

  def sort(self, map_to_key=lambda x : x, descending=False):
    """ sort
      Sorts the list in-place using insertion algorithm.
      Default is to sort in ascending order.

      map_to_key: an optional mapping function from the stored
        object type to the key to sort by with.

      descending: an optional boolean to declare if the sort
      should be descending rather than ascending.
    """
    def _insertion_sort(front):
      #if the linkedlist is empty or has only one node, therefore, is already sorted
      if not front or not front.next:
          return front
      
      sorted_list = None #initialize the sorted list as empty
      cur = front #start traversing the list at the front 
      
      if descending: #if descending is True -- call rev_insert()
        
        #start the loop at the cur which points to front
        while cur:
            next_node = cur.next #storing next_node temporarily 
            sorted_list = _rev_insert(sorted_list, cur) #call rev_insert() -- insert current node into the reverse sorted list
            cur = next_node #move to the next node in the orginal list
        
        return sorted_list
      
      else: #else descending is False -- call regular insert()
        while cur:
            next_node = cur.next
            sorted_list = _insert(sorted_list, cur)
            cur = next_node
        
        return sorted_list

    def _insert(sorted_list, new_node):
      #if the sorted list is empty of cur node is smaller, then insert at the beginning
      if not sorted_list or map_to_key(sorted_list.data) >= map_to_key(new_node.data):
          #insert to beginning
          new_node.next = sorted_list
          return new_node
      
      cur = sorted_list
      
      # find the right position to insert the new node, following the condition that is the current node is less than the new_node
      while cur.next and map_to_key(cur.next.data) < map_to_key(new_node.data):
          #update cur
          cur = cur.next
      
      # insert thge new node in the appropriate position  
      new_node.next = cur.next
      cur.next = new_node
      
      return sorted_list
  
    def _rev_insert(sorted_list, new_node):
      #if new_node not in sorted_list -- or -- sorted_list.data is less than the inputed new_node data
      if not sorted_list or map_to_key(sorted_list.data) < map_to_key(new_node.data):
          #point new_node.next to sorted_list
          new_node.next = sorted_list
          return new_node
      
      cur = sorted_list
      #loop cur.next -- and -- cur.data (node.data in the sorted_list) greater than or equal to inputed new_node data
      while cur.next and map_to_key(cur.next.data) >= map_to_key(new_node.data):
          #update cur variable
          cur = cur.next
      
      # insert thge new node in the appropriate position  
      new_node.next = cur.next
      cur.next = new_node
      
      return sorted_list
      
    self._front = _insertion_sort(self._front)
    

