class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.right__child = None
      self.left__child  = None
      self.height = 1

    # def _retrieve_balance(self):
    # Checks the balance of the tree by comparing the left and 
    # right childen's height.
    # If both left and right children are none, return 0
    # If either left or right child are none, return the opposite child's height
    def _retrieve_balance(self):
    
        if self.left__child is None and self.right__child is None:
            return 0
        elif self.left__child is None:
            return self.right__child.height
        elif self.right__child is None:
            return 0 - self.left__child.height
        else:
            return self.right__child.height - self.left__child.height
            
    # def _every_height(self):
    # Retrieves height of every child by checking if we have both, or either left
    # right children
    def _every_height(self):
    
        if (self.left__child and self.right__child is None):
            self.height = self.left__child.height + 1 
        elif (self.right__child and self.left__child is None): 
            self.height = self.right__child.height + 1  
        elif (self.right__child is None and self.left__child is None):
            self.height = 1
        elif (self.left__child.height >= self.right__child.height):
            self.height = self.left__child.height + 1    
        else:
            self.height = self.right__child.height + 1

  # def __balance(self, current_node):
  # Sets a variable to the balance of tree and checks if either are
  # between +/- 2. If it is equal to 2, then it balances to the left
  # otherwise if it is -2 it balances to the right.
  # It then retireves the child's balance and rotates accordingly to
  # either the left or right, depending on which is needing to be rotated.
  def __balance(self, current_node):
      
        current_balance = current_node._retrieve_balance()
        if (current_balance < 2 and current_balance > -2):
            return current_node
        if (current_balance == 2):
            right_balance = current_node.right__child._retrieve_balance()
            if (right_balance == 1 or right_balance == 0):
                return self._rotate_right(current_node)
            elif (right_balance == -1):
                current_node.right__child = self._rotate_left(current_node.right__child)
                return self._rotate_right(current_node)
        if (current_balance == -2):
            left_balance = current_node.left__child._retrieve_balance()
            if (left_balance == -1 or left_balance == 0):
                return self._rotate_left(current_node)
            elif (left_balance == 1):
                current_node.left__child = self._rotate_right(current_node.left__child)
                return self._rotate_left(current_node)

  # def _rotate_right(self, node):
  # Has variables which are set to the left and parent nodes
  # If we are in the nodes left child of right child then we set the right 
  # child to the right child's left child
  # Otherwise we just set it equal to None
  # Set the left child of new parent node equal to the left node
  # Get the height for both
  # And return updated parent node to the root
  def _rotate_right(self, node):
      
      left_node = node
      parent_node = node.right__child
      if (node.right__child.left__child):
          left_node.right__child = node.right__child.left__child
      else:
          left_node.right__child = None
      parent_node.left__child = left_node
      left_node._every_height()
      parent_node._every_height()
      return parent_node

  # def _rotate_left(self, node):
  # Set variables equal to the right node and parent node
  # If we are in the node's left child's right child
  # Set the left child of the right node to the passed node's right child of left child
  # Otherwise the left node is equal to None
  # Set the parent node's right child to the variable
  # Retrieve the indidividual heights
  # Update the information to the root node
  def _rotate_left(self, node):
    
      right_node = node
      parent_node = node.left__child
      if (node.left__child.right__child):
          right_node.left__child = node.left__child.right__child
      else:
          right_node.left__child = None
      parent_node.right__child = right_node
      right_node._every_height()
      parent_node._every_height()
      return parent_node
  
  # def __init__(self):
  # Initialize the root and set tree 
  def __init__(self):
    self.__root = None
    self.__tree = 0

  # def insert_element(self, value):
  # Filling up the tree with the private insertion recursive method
  # Making the tree equal to the height of passed in variables
  def insert_element(self, value):
      self.__root = self._recursive_insert(self.__root, value)
      self.__tree = self._height(self.__root) 
  
  # def _recursive_insert(self, current_node, value):
  # If in the current node being passed
  # Raise a value error if the value is already in the tree
  # Otherwise check if the value is greater than the current nodes value
  # If yes then keep on recursing
  # Otherwise base case, insert new node with value
  # If it is less than, go to the right child
  # If in the right child and value is less than current node
  # Keep on recursing 
  # Otherwise base case, insert new node
  # If neither, then current node is the root, and insert the value
  # Get height of the tree and return the balance
  def _recursive_insert(self, current_node, value):
    
    if (current_node):
        if (current_node.value == value):
            raise ValueError
        elif (current_node.value > value):
            if (current_node.left__child):
                current_node.left__child = self. _recursive_insert(current_node.left__child, value)
            else:
                current_node.left__child = self.__BST_Node(value)
        else:
            if (current_node.right__child):       
                current_node.right__child = self. _recursive_insert(current_node.right__child, value)   
            else:
                current_node.right__child = self.__BST_Node(value)
    else: 
        current_node = self.__BST_Node(value)
    current_node._every_height()
    return self.__balance(current_node)

  # def remove_element(self, value):
  # Start from root and do the removal
  # if the root, set the tree to the height of the root
  def remove_element(self, value):
      
    self.__root = self._recursive_removal(self.__root, value)
    if (self.__root):
        self.__tree = self._height(self.__root)
  
  # def _recursive_removal(self, current_node, value):
  # If the node has no value raise error or
  # if the node's value is equal to the value
  # and if the node has nothing then return it
  # But If the value is less then go to the left
  # Do the recursion and update the height
  # If it is greater then go to the right
  # Do recursion and update the height
  # Return the balance of the node
  def _recursive_removal(self, current_node, value):
      
    if (current_node is None):
        raise ValueError
    if (current_node.value == value):
        current_node = self._remove(current_node)
        if (current_node is None):
            return current_node
    elif (value < current_node.value):
        current_node.left__child = self._recursive_removal(current_node.left__child, value)
        current_node._every_height()
    elif (value > current_node.value):
        current_node.right__child = self._recursive_removal(current_node.right__child, value)
        current_node._every_height()
    return self.__balance(current_node)

  # def _remove(self, current_node):
  # If both left and right children are None, then return None
  # or if there is a left child but no right, then return the left child
  # or if there is a right child, but no left, then return right child
  # Otherwise make a variable equal to the right child
  # And while in the left child, we make the variable equal to the right child's left child
  # We make the value equal to the node being removed value
  # Recursively go through, passing the value of the passed-in node, with the right child
  # And return the updated node to the root
  def _remove(self, current_node):

      if (current_node.left__child is None and current_node.right__child is None):
          return None
      elif (current_node.left__child and current_node.right__child is None):
          return current_node.left__child
      elif (current_node.left__child is None and current_node.right__child):
          return current_node.right__child
      else:
          removeNode = current_node.right__child
          while (removeNode.left__child):
              removeNode = removeNode.left__child
          current_node.value = removeNode.value
          current_node.right__child = self._recursive_removal(current_node.right__child, current_node.value)
          return current_node

  # def in_order(self):
  # Returns the in-order format
  def in_order(self):
    return self._in_order()

  # def _in_order(self):
  # If there is no value in the root
  # return an empty set, otherwise
  # set a string variable with open brackets
  # Set string equal to the recursion method's values
  # String the values in the variable, using slicing and end the string
  # return the string
  def _in_order(self):

    if (self.__root is None):
      return "[ ]"
    else:
      string_in_order = "[ "
      string_in_order = self._print_in_order(self.__root, string_in_order)
      string_in_order = string_in_order[0:-2] + " ]"
      return string_in_order
  
  # def _print_in_order(self, current_node, string_in_order):
  # If the current right child is not none
  # set the string variable to the recursively printing the statement
  # if the left child is equal to none 
  # Set the string variable to the string variable plus the string separated by comma
  # Otherwise, string the variable with the left child and separate by comma
  # return the string variable
  def _print_in_order(self, current_node, string_in_order):

    if (current_node.right__child is not None):
      string_in_order = self._print_in_order(current_node.right__child, string_in_order)
    if (current_node.left__child is None):
      string_in_order = string_in_order + str(current_node.value) + ", "
    else:
      string_in_order = self._print_in_order(current_node.left__child, string_in_order)
      string_in_order = string_in_order + str(current_node.value) + ", "
    return string_in_order


  # def pre_order(self):
  # Returns the pre-order format
  def pre_order(self):
    return self._pre_order()

  # def _pre_order(self):
  # If the root node is none, return an empty set
  # Otherwise create a string variable
  # set the variable to the recursive method of pre-order
  # set the variable to the values and close the bracket
  # return the string
  def _pre_order(self):

    if (self.__root == None):
      return "[ ]"
    else:
      string_pre_order = "[ "
      string_pre_order = self._print_pre_order(self.__root, string_pre_order)
      string_pre_order = string_pre_order[0:-2] + " ]"
      return string_pre_order

  # def _print_pre_order(self, current_node, string_pre_order):
  # Set the string variable to the string and the value of current node separate by comma
  # If the left child is not none set the string to the recursive for the left children
  # If the current node right child is not none
  # set the string variable to the recursive values in the method
  # return the string variable
  def _print_pre_order(self, current_node, string_pre_order):

    string_pre_order = string_pre_order + str(current_node.value) + ", "
    if(current_node.left__child is not None):
      string_pre_order = self._print_pre_order(current_node.left__child, string_pre_order)
    if(current_node.right__child is not None):
      string_pre_order = self._print_pre_order(current_node.right__child, string_pre_order)
    return string_pre_order

  # def post_order(self):
  # Returns post-order format
  def post_order(self):
    return self._post_order()

  # def _post_order(self):
  # If the root is equal to none, return empty string
  # Set string variable to open bracket
  # set the string variable equal to the returned values in the recursive method
  # set the variable equal to the values and close the bracket
  # return the string variable
  def _post_order(self):

    if (self.__root is None):
      return "[ ]"
    
    else:
      string_post_order = "[ "
      string_post_order = self._print_post_order(self.__root, string_post_order)
      string_post_order = string_post_order[0:-2] + " ]"
      return string_post_order

  # def _print_post_order(self, current_node, string_post_order):
  # If the left child is not none, set the string variable equal to the recursive method values
  # If the right child is none, set the string variable to the values of the node separate by comma
  # Set the string variable to the returned values in the recursive method
  # Set the variable to the values separated by comma and return the string
  def _print_post_order(self, current_node, string_post_order):

    if (current_node.left__child is not None):
      string_post_order = self._print_post_order(current_node.left__child, string_post_order)
    if (current_node.right__child is None):
      string_post_order = string_post_order + str(current_node.value) + ", "
    else:
      string_post_order = self._print_post_order(current_node.right__child, string_post_order)
      string_post_order = string_post_order + str(current_node.value) + ", "
    return string_post_order

  # def get_height(self):
  # If in the root, then return the tree
  # Otherwise it is empty and return 0
  def get_height(self):

    if (self.__root):
        return self.__tree
    else: 
        return 0

  # def _height(self, current_node):
  # If we have both left and right children
  # Then we check the heights of them both, returning the left child's height, or the right child's height + 1 for root
  # If we only have a left child, then return 1 (for root) plus the height of left child
  # If we have only a right, return 1 (for root) plus the height of the right child
  # If we have neither, our root is of height 1, so return 1
  def _height(self, current_node):

    if (current_node.left__child and current_node.right__child):
         if (self._height(current_node.left__child) >= self._height(current_node.right__child)):
             return 1 + self._height(current_node.left__child)
         else:
             return 1 + self._height(current_node.right__child)
    elif (current_node.left__child):
         return 1 + self._height(current_node.left__child)
    elif(current_node.right__child):
         return 1 + self._height(current_node.right__child)
    else:
         return 1

  # def to_list(self): 
  # Make a variable to a list
  # If the root does not have anything in it, then return the empty list
  # Otherwise if both of our children are None, but have a value in root, return the root value
  # If we have at least one, then go thorugh the recursive function adding them to our list
  # Once done, return the ordered list
  def to_list(self):

      list_in_order = list()
      if (self.__root is None):
          return list_in_order
      elif( self.__root.left__child is None and self.__root.right__child is None):
          list_in_order.append(self.__root.value)
      else:
          list_in_order += self.__in_order_recursion(self.__root)
      return list_in_order

  # def __in_order_recursion(self, current_node):
  # If we have both the left and right child
  # Return the left child, the current node's value, and the right child
  # If we have only the left child then return the left child and it's value
  # If we have only a right child then return the value of the node, and the right child's value
  # Base case, return the node's value
  def __in_order_recursion(self, current_node):

      if (current_node.left__child and current_node.right__child):
          return self.__in_order_recursion(current_node.left__child) + [current_node.value] + self.__in_order_recursion(current_node.right__child)
      elif (current_node.left__child):
          return self.__in_order_recursion(current_node.left__child) + [current_node.value]
      elif (current_node.right__child):
          return [current_node.value] + self.__in_order_recursion(current_node.right__child)
      else:
          return [current_node.value]

  # def __str__(self):
  # Returns the string method by defaulting it to in-order format.
  def __str__(self):
    return self.in_order()

# if __name__ == '__main__':
#  pass #unit tests make the main section unnecessary.