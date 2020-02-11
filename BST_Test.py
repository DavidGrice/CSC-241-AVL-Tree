import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):

    def setUp(self):
        self.__BST = Binary_Search_Tree()

    def test_Empty_Cases(self):
        self.assertEqual('[ ]', str(self.__BST), "Empty Tree (In-Order) should be printed '[ ]'")
        self.assertEqual('[ ]', self.__BST.pre_order(), "Empty Tree (Pre-Order) should be printed '[ ]'")
        self.assertEqual('[ ]', self.__BST.post_order(), "Empty Tree (Post-Order) should be printed '[ ]'")

    def test_Remove_Method(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(20)
        self.assertEqual('[ ]', str(self.__BST), "Should raise a ValueError")

    def test_Height_Insert_Remove(self):
        self.assertEqual(0, self.__BST.get_height(), "Empty tree should have 0 height")
        self.__BST.insert_element(1)
        self.assertEqual(1, self.__BST.get_height(), "Height should be 1")
        self.__BST.remove_element(1)
        self.assertEqual(0, self.__BST.get_height(), "Height should be 0")

    def test_Left_Tree_String_Output(self):
        for l in range (9, 0, -1):
            self.__BST.insert_element(l)
        self.assertEqual("[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]", str(self.__BST), "In-Order fails test")
        self.assertEqual("[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]", self.__BST.pre_order(), "Pre-Order fails test")
        self.assertEqual("[ 9, 8, 7, 6, 5, 4, 3, 2, 1 ]", self.__BST.post_order(), "Post-Order fails test")

    def test_Right_Tree_String_Output(self):
        for r in range(1, 10):
            self.__BST.insert_element(r)
        self.assertEqual("[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]", str(self.__BST), "In-Order fails test")
        self.assertEqual("[ 9, 8, 7, 6, 5, 4, 3, 2, 1 ]", self.__BST.post_order(), "Post-Order fails test")
        self.assertEqual("[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]", self.__BST.pre_order(), "Pre-Order fails test")

    def test_Remove_Node_With_One_Child(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(18)
        self.__BST.insert_element(28)
        self.__BST.insert_element(12)
        self.__BST.insert_element(21)
        self.__BST.insert_element(30)
        self.assertEqual("[ 12, 18, 21, 25, 28, 30 ]", str(self.__BST), "In-Order fails test")
        self.__BST.remove_element(28)
        self.assertEqual("[ 12, 18, 21, 25, 30 ]", str(self.__BST), "In-Order fails test")
        self.assertEqual("[ 25, 18, 12, 21, 30 ]", self.__BST.pre_order(), "Pre-Order fails test")
        self.assertEqual("[ 12, 21, 18, 30, 25 ]", self.__BST.post_order(), "Post-Order fails test")

    def test_Height_Of_Tree_And_String(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(18)
        self.__BST.insert_element(18.72)
        self.__BST.insert_element(19)
        self.__BST.insert_element(26)
        self.__BST.insert_element(49)
        self.__BST.insert_element(1693)
        self.assertEqual("[ 5, 18, 18.72, 19, 26, 49, 1693 ]", str(self.__BST), "In-Order fails the test")
        self.assertEqual("[ 19, 18, 5, 18.72, 49, 26, 1693 ]", self.__BST.pre_order(), "Pre-Order fails the test")
        self.assertEqual("[ 5, 18.72, 18, 26, 1693, 49, 19 ]", self.__BST.post_order(), "Post-Order fails the test")
        self.assertEqual(7, self.__BST.get_height(), "Height should be 7")

    def test_Height_Of_Tree(self):
        for high in range(1, 1000):
            self.__BST.insert_element(high)
        self.assertEqual(999, self.__BST.get_height(), "Height should be 99")

    def test_Insert_Value_Already_Stored_In_Tree(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(2)
        self.__BST.insert_element(4)
        self.__BST.insert_element(6)
        self.__BST.insert_element(8)
        self.__BST.insert_element(10)
        self.__BST.insert_element(-1)
        self.__BST.insert_element(-3)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(-7)
        self.__BST.insert_element(-9)
        self.__BST.insert_element(-11)
        with self.assertRaises(ValueError):
            self.__BST.insert_element(8)
    
    def test_Value_Error(self):
      with self.assertRaises(ValueError):
          self.__BST.remove_element(5)
      self.assertEqual('[ ]', str(self.__BST), 'Should raise ValueError')

    def test_Removing_Leaf_Node(self):
      self.__BST.insert_element(26)
      self.__BST.insert_element(19)
      self.__BST.insert_element(29)
      self.__BST.insert_element(13)
      self.__BST.insert_element(22)
      self.__BST.insert_element(31)
      self.assertEqual('[ 13, 19, 22, 26, 29, 31 ]', str(self.__BST), 'in_order before removal format fails')
      self.__BST.remove_element(13)
      self.assertEqual('[ 19, 22, 26, 29, 31 ]', str(self.__BST), 'in_order after removal format fails')
      self.assertEqual('[ 26, 19, 22, 29, 31 ]', self.__BST.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 22, 19, 31, 29, 26 ]', self.__BST.post_order(), 'post_order after removal format fails')

    def test_Removing_Node_With_One_Child(self):
      self.__BST.insert_element(26)
      self.__BST.insert_element(19)
      self.__BST.insert_element(29)
      self.__BST.insert_element(13)
      self.__BST.insert_element(22)
      self.__BST.insert_element(31)
      self.assertEqual('[ 13, 19, 22, 26, 29, 31 ]', str(self.__BST), 'in_order before removal format fails')
      self.__BST.remove_element(29)
      self.assertEqual('[ 13, 19, 22, 26, 31 ]', str(self.__BST), 'in_order after removal format fails')
      self.assertEqual('[ 26, 19, 13, 22, 31 ]', self.__BST.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 13, 22, 19, 31, 26 ]', self.__BST.post_order(), 'post_order after removal format fails') 


    def test_Removing_Leaf_Nodes_And_Testing_Height(self):
      self.__BST.insert_element(2)
      self.__BST.insert_element(9)
      self.__BST.insert_element(92)
      self.__BST.insert_element(31)
      self.__BST.insert_element(51)
      self.__BST.insert_element(27)
      self.assertEqual(3, self.__BST.get_height(), 'Height should be 3')
      self.__BST.remove_element(31)
      self.__BST.remove_element(2)
      self.__BST.remove_element(27)
      self.assertEqual(2, self.__BST.get_height(), 'Height should be 2')

    def test_Removing_Value_Not_In_Tree(self):
      for i in range(1, 10):
          if i%2 == 1:
              self.__BST.insert_element(i)
      for i in range(1, 10):
          if i%2 == 0:
              self.__BST.insert_element(i)
      self.__BST.insert_element(30)
      self.__BST.insert_element(5)
      self.__BST.insert_element(2)
      self.__BST.insert_element(77)
      self.__BST.insert_element(56)
      self.__BST.insert_element(35)
      with self.assertRaises(ValueError):
        self.__BST.remove_element(12)

    def test_Inserting_Value_Already_Inside_Tree(self):
      for i in range(1, 10):
          if i%2 == 1:
              self.__BST.insert_element(i)
      for i in range(1, 10):
          if i%2 == 0:
              self.__BST.insert_element(i)
      self.__BST.insert_element(62)
      self.__BST.insert_element(91)
      self.__BST.insert_element(92)
      self.__BST.insert_element(31)
      self.__BST.insert_element(2)
      self.__BST.insert_element(10)
      with self.assertRaises(ValueError):
        self.__BST.insert_element(92)

    def test_Removing_Nodes_Two_Children_And__Getting_Height(self):
      self.__BST.insert_element(2) 
      self.__BST.insert_element(91) 
      self.__BST.insert_element(40) 
      self.__BST.insert_element(10)  
      self.__BST.insert_element(100.67)   
      self.__BST.insert_element(72) 
      self.__BST.insert_element(1693)   
      self.assertEqual('[ 10, 91, 100.67, 2, 72, 40, 1693 ]', str(self.__BST), 'in_order before removal format fails')
      self.assertEqual('[ 2, 91, 10, 100.67, 40, 72, 1693 ]', self.__BST.pre_order(), 'pre_order before removal format fails')
      self.assertEqual('[ 10, 100.67, 91, 72, 1693, 40, 2 ]', self.__BST.post_order(), 'post_order before removal format fails')
      self.assertEqual(3, self.__BST.get_height(), 'Height should be 3')
      self.__BST.remove_element(20)
      self.assertEqual('[ 10, 91, 100.67, 72, 40, 1693 ]', str(self.__BST), 'in_order after removal format fails')
      self.assertEqual('[ 72, 91, 10, 100.67, 40, 1693 ]', self.__BST.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 10, 100.67, 91, 1693, 40, 72 ]', self.__BST.post_order(), 'post_order after format fails')
      self.assertEqual(3, self.__BST.get_height(), 'Height after removal of root should be 3')


if __name__ == '__main__':
    unittest.main()