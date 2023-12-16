import unittest
from list.linked_list import LinkedList


class TestLinkedListBase(unittest.TestCase):
    """ Base case - sets up initial values to test """

    def setUp(self):
        """sets up values before each unit test"""

        # a typical case - numbers
        self._typical1_int = LinkedList()
        self._typical1_int.append(5)
        self._typical1_int.append(9)
        self._typical1_int.append(0)
        self._typical1_int.append(4)
        self._typical1_int.append(5)
        self._typical1_int.append(-2)

        # a typical case - tuples (to test maps)
        self._typical2_tuple = LinkedList()
        self._typical2_tuple.append( ('Latte', 5.49) )
        self._typical2_tuple.append( ('Drip Coffee', 2.19) )
        self._typical2_tuple.append( ('Caramel Frappuccino', 6.79) )

        # an unusual case (empty)
        self._unusual1_empty = LinkedList()

        # an unusual case (one item)
        self._unusual2_oneitem = LinkedList()
        self._unusual2_oneitem.append("oneitem")




#####################
#    Constructor    #
#####################

class TestLinkedListConstructor(TestLinkedListBase):
    """ Tests for the constructor """

    def test_constructor_noerrors(self):
        """ Test for no errors"""
        newLinkedList = LinkedList()

    def test_constructor_initialstate(self):
        """ Test initial state via accessors """
        newLinkedList = LinkedList()
        self.assertEqual(0, newLinkedList.length())
        self.assertEqual(-1, newLinkedList.find_index_byvalue(99))
        self.assertEqual(False, newLinkedList.contains(99))
        with self.assertRaises(IndexError):
            newLinkedList.get(0)


###################
#    Accessors    #
###################

class TestLinkedListLength(TestLinkedListBase):
    """ Tests for length() """

    def test_length_typical1(self):
        self.assertEqual(6, self._typical1_int.length())

    def test_length_typical2(self):
        self.assertEqual(3, self._typical2_tuple.length())

    def test_length_unusual1_empty(self):
        self.assertEqual(0, self._unusual1_empty.length())

    def test_length_unusual2_length1(self):
        self.assertEqual(1, self._unusual2_oneitem.length())


class TestLinkedListContains(TestLinkedListBase):
    """ Tests for contains() """

    def test_contains_typical1(self):
        # true results
        self.assertTrue(self._typical1_int.contains(5))
        self.assertTrue(self._typical1_int.contains(9))
        self.assertTrue(self._typical1_int.contains(0))
        self.assertTrue(self._typical1_int.contains(4))
        self.assertTrue(self._typical1_int.contains(-2))

        #false results
        self.assertFalse(self._typical1_int.contains(-1))
        self.assertFalse(self._typical1_int.contains(100))

    def test_contains_typical2(self):
        # true results
        self.assertTrue(self._typical2_tuple.contains( ('Latte', 5.49) ))
        self.assertTrue(self._typical2_tuple.contains( ('Drip Coffee', 2.19) ))
        self.assertTrue(self._typical2_tuple.contains( ('Caramel Frappuccino', 6.79) ))

        #false results
        self.assertFalse(self._typical2_tuple.contains( ('Orange Mocha Frappuccino', 8.29) ))
        self.assertFalse(self._typical2_tuple.contains( ('Donut', 0.99) ))

    def test_contains_typical2_keymap(self):
        # true results
        map_to_first_key = lambda x : x[0]
        self.assertTrue(self._typical2_tuple.contains( 'Latte', map_to_key=map_to_first_key ))
        self.assertTrue(self._typical2_tuple.contains( 'Drip Coffee', map_to_key=map_to_first_key ))
        self.assertTrue(self._typical2_tuple.contains( 'Caramel Frappuccino', map_to_key=map_to_first_key ))


        map_to_second_key = lambda x : x[1]
        self.assertTrue(self._typical2_tuple.contains( 5.49, map_to_key=map_to_second_key ))
        self.assertTrue(self._typical2_tuple.contains( 2.19, map_to_key=map_to_second_key ))
        self.assertTrue(self._typical2_tuple.contains( 6.79, map_to_key=map_to_second_key ))

        #false results
        self.assertFalse(self._typical2_tuple.contains( 'Orange Mocha Frappuccino', map_to_key=map_to_first_key ))
        self.assertFalse(self._typical2_tuple.contains( 'Donut', map_to_key=map_to_first_key ))

        self.assertFalse(self._typical2_tuple.contains( 8.29, map_to_key=map_to_second_key ))
        self.assertFalse(self._typical2_tuple.contains( 0.99, map_to_key=map_to_second_key ))


    def test_contains_unusual1_empty(self):
        # false results
        self.assertFalse(self._unusual1_empty.contains(5))
        self.assertFalse(self._unusual1_empty.contains(9))
        self.assertFalse(self._unusual1_empty.contains(0))
        self.assertFalse(self._unusual1_empty.contains(4))
        self.assertFalse(self._unusual1_empty.contains(-2))

        self.assertFalse(self._unusual1_empty.contains(-1))
        self.assertFalse(self._unusual1_empty.contains(100))

        self.assertFalse(self._unusual1_empty.contains( ('Latte', 5.49) ))
        self.assertFalse(self._unusual1_empty.contains( ('Drip Coffee', 2.19) ))
        self.assertFalse(self._unusual1_empty.contains( ('Caramel Frappuccino', 6.79) ))

        self.assertFalse(self._unusual1_empty.contains( ('Orange Mocha Frappuccino', 8.29) ))
        self.assertFalse(self._unusual1_empty.contains( ('Donut', 0.99) ))
        

    def test_contains_unusual2_length1(self):
        # true results
        self.assertTrue(self._unusual2_oneitem.contains("oneitem"))

        # false results
        self.assertFalse(self._unusual2_oneitem.contains("twoitem"))
        self.assertFalse(self._unusual2_oneitem.contains(""))


class TestLinkedListFind(TestLinkedListBase):
    """ Tests for find_index_by_value() """

    def test_find_typical1(self):
        self.assertEqual(0, self._typical1_int.find_index_byvalue(5))
        self.assertEqual(1, self._typical1_int.find_index_byvalue(9))
        self.assertEqual(2, self._typical1_int.find_index_byvalue(0))
        self.assertEqual(3, self._typical1_int.find_index_byvalue(4))
        self.assertEqual(0, self._typical1_int.find_index_byvalue(5))
        self.assertEqual(5, self._typical1_int.find_index_byvalue(-2))

        self.assertEqual(-1, self._typical1_int.find_index_byvalue(-1))
        self.assertEqual(-1, self._typical1_int.find_index_byvalue(100))

    def test_find_typical2(self):
        # true results
        self.assertEqual(0, self._typical2_tuple.find_index_byvalue( ('Latte', 5.49) ))
        self.assertEqual(1, self._typical2_tuple.find_index_byvalue( ('Drip Coffee', 2.19) ))
        self.assertEqual(2, self._typical2_tuple.find_index_byvalue( ('Caramel Frappuccino', 6.79) ))

        #false results
        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( ('Orange Mocha Frappuccino', 8.29) ))
        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( ('Donut', 0.99) ))

    def test_find_typical2_keymap(self):
        # found results
        map_to_first_key = lambda x : x[0]
        self.assertEqual(0, self._typical2_tuple.find_index_byvalue( 'Latte', map_to_key=map_to_first_key ))
        self.assertEqual(1, self._typical2_tuple.find_index_byvalue( 'Drip Coffee', map_to_key=map_to_first_key ))
        self.assertEqual(2, self._typical2_tuple.find_index_byvalue( 'Caramel Frappuccino', map_to_key=map_to_first_key ))


        map_to_second_key = lambda x : x[1]
        self.assertEqual(0, self._typical2_tuple.find_index_byvalue( 5.49, map_to_key=map_to_second_key ))
        self.assertEqual(1, self._typical2_tuple.find_index_byvalue( 2.19, map_to_key=map_to_second_key ))
        self.assertEqual(2, self._typical2_tuple.find_index_byvalue( 6.79, map_to_key=map_to_second_key ))

        # not found
        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( 'Orange Mocha Frappuccino', map_to_key=map_to_first_key ))
        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( 'Donut', map_to_key=map_to_first_key ))

        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( 8.29, map_to_key=map_to_second_key ))
        self.assertEqual(-1, self._typical2_tuple.find_index_byvalue( 0.99, map_to_key=map_to_second_key ))


    def test_find_unusual1_empty(self):
        # not found
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(5))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(9))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(0))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(4))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(-2))

        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(-1))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue(100))

        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue( ('Latte', 5.49) ))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue( ('Drip Coffee', 2.19) ))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue( ('Caramel Frappuccino', 6.79) ))

        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue( ('Orange Mocha Frappuccino', 8.29) ))
        self.assertEqual(-1, self._unusual1_empty.find_index_byvalue( ('Donut', 0.99) ))

    def test_find_unusual2_length1(self):
        # found
        self.assertEqual(0, self._unusual2_oneitem.find_index_byvalue("oneitem"))

        # not found
        self.assertEqual(-1, self._unusual2_oneitem.find_index_byvalue("twoitem"))
        self.assertEqual(-1, self._unusual2_oneitem.find_index_byvalue(""))


class TestLinkedListGet(TestLinkedListBase):
    """ Tests for get() """

    def test_get_typical1(self):
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

    def test_get_typical1_error(self):
        with self.assertRaises(IndexError):
            self._typical1_int.get(-1)

        with self.assertRaises(IndexError):
            self._typical1_int.get(6)

        with self.assertRaises(IndexError):
            self._typical1_int.get(7)

        with self.assertRaises(IndexError):
            self._typical1_int.get(100)

    def test_get_typical2(self):
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

    def test_get_typical2_error(self):
        with self.assertRaises(IndexError):
            self._typical2_tuple.get(-1)

        with self.assertRaises(IndexError):
            self._typical2_tuple.get(3)

        with self.assertRaises(IndexError):
            self._typical2_tuple.get(4)

        with self.assertRaises(IndexError):
            self._typical2_tuple.get(100)


    def test_get_unusual1_empty(self):
        with self.assertRaises(IndexError):
            self._unusual1_empty.get(-1)

        with self.assertRaises(IndexError):
            self._unusual1_empty.get(0)

        with self.assertRaises(IndexError):
            self._unusual1_empty.get(1)

        with self.assertRaises(IndexError):
            self._unusual1_empty.get(100)

    def test_get_unusual2_length1(self):
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        with self.assertRaises(IndexError):
            self._unusual2_oneitem.get(1)



##################
#    Mutators    #
##################

class TestLinkedListSet(TestLinkedListBase):
    """ Tests for set() """

    def test_set_typical1(self):
        # check initial state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.set(2, 99)

        # check follow-up state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(99, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.set(3, 45)

        # check follow-up state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(99, self._typical1_int.get(2))
        self.assertEqual(45, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.set(0, -100)

        # check follow-up state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(-100, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(99, self._typical1_int.get(2))
        self.assertEqual(45, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.set(5, -99)

        # check follow-up state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(-100, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(99, self._typical1_int.get(2))
        self.assertEqual(45, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-99, self._typical1_int.get(5))


    def test_set_typical1_error(self):
        with self.assertRaises(IndexError):
            self._typical1_int.set(-1, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(6, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(7, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(100, 99)

    def test_set_typical2(self):
        # test initial state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.set(0, ('Chai Latte', 5.85))

        # test follow-up state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.set(1, ('Soy Chai Latte', 6.35))

        # test follow-up state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(0) )
        self.assertEqual( ('Soy Chai Latte', 6.35), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.set(2, ('Oat Milk Chai Latte', 6.35))

        # test follow-up state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(0) )
        self.assertEqual( ('Soy Chai Latte', 6.35), self._typical2_tuple.get(1) )
        self.assertEqual( ('Oat Milk Chai Latte', 6.35), self._typical2_tuple.get(2) )

    def test_set_typical2_error(self):
        with self.assertRaises(IndexError):
            self._typical2_tuple.set(-1, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.set(3, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.set(4, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.set(100, ('Chai Latte', 5.85))

    def test_set_unusual1_empty(self):
        with self.assertRaises(IndexError):
            self._unusual1_empty.set(-1, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.set(0, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.set(1, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.set(100, 99)

    def test_set_unusual2_length1(self):
        # test initial state
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        self._unusual2_oneitem.set(0, "only this")

        # test follow-up state
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("only this", self._unusual2_oneitem.get(0))

        self._unusual2_oneitem.set(0, "now just this")

        # test follow-up state
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("now just this", self._unusual2_oneitem.get(0))

    def test_set_unusual2_length1_error(self):
        with self.assertRaises(IndexError):
            self._unusual2_oneitem.set(1, "twoitem")

        with self.assertRaises(IndexError):
            self._unusual2_oneitem.set(2, "twoitem")

        with self.assertRaises(IndexError):
            self._unusual2_oneitem.set(100, "twoitem")

        with self.assertRaises(IndexError):
            self._unusual2_oneitem.set(-1, "twoitem")
        


class TestLinkedListAppend(TestLinkedListBase):
    """ Tests for append() """

    def test_append_typical1(self):
        # check initial state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.append(99)

        # check follow-up state
        self.assertEqual(7, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self.assertEqual(99, self._typical1_int.get(6))

        self._typical1_int.append(-99)

        # test follow-up state
        self.assertEqual(8, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self.assertEqual(99, self._typical1_int.get(6))
        self.assertEqual(-99, self._typical1_int.get(7))

    def test_append_typical2(self):
        # test initial state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.append(('Chai Latte', 5.85))

        # test follow-up state
        self.assertEqual(4, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(3) )

        self._typical2_tuple.append(('Soy Chai Latte', 6.35))

        # test follow-up state
        self.assertEqual(5, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(3) )
        self.assertEqual( ('Soy Chai Latte', 6.35), self._typical2_tuple.get(4) )

    def test_append_unusual1_empty(self):
        # test initial state
        self.assertEqual(0, self._unusual1_empty.length())

        self._unusual1_empty.append(101)

         # test follow-up state
        self.assertEqual(1, self._unusual1_empty.length())
        self.assertEqual(101, self._unusual1_empty.get(0))

    def test_append_unusual2_length1(self):
        # test initial state
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        self._unusual2_oneitem.append("twoitem")
        
        # test follow-up state
        self.assertEqual(2, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))
        self.assertEqual("twoitem", self._unusual2_oneitem.get(1))

        self._unusual2_oneitem.append("threeitem")
        
        # test follow-up state
        self.assertEqual(3, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))
        self.assertEqual("twoitem", self._unusual2_oneitem.get(1))
        self.assertEqual("threeitem", self._unusual2_oneitem.get(2))


class TestLinkedListInsert(TestLinkedListBase):
    """ Tests for insert() """

    def test_insert_typical1(self):
        # check initial state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self._typical1_int.insert(2, 101)

        # check follow-up state
        self.assertEqual(7, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(101, self._typical1_int.get(2))
        self.assertEqual(0, self._typical1_int.get(3))
        self.assertEqual(4, self._typical1_int.get(4))
        self.assertEqual(5, self._typical1_int.get(5))
        self.assertEqual(-2, self._typical1_int.get(6))

        self._typical1_int.insert(5, 102)

        # check follow-up state
        self.assertEqual(8, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(101, self._typical1_int.get(2))
        self.assertEqual(0, self._typical1_int.get(3))
        self.assertEqual(4, self._typical1_int.get(4))
        self.assertEqual(102, self._typical1_int.get(5))
        self.assertEqual(5, self._typical1_int.get(6))
        self.assertEqual(-2, self._typical1_int.get(7))

    def test_insert_typical1_edgecases(self):
        # check initial state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        # insert at front
        self._typical1_int.insert(0, 101)

        # check follow-up state
        self.assertEqual(7, self._typical1_int.length())
        self.assertEqual(101, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))
        self.assertEqual(9, self._typical1_int.get(2))
        self.assertEqual(0, self._typical1_int.get(3))
        self.assertEqual(4, self._typical1_int.get(4))
        self.assertEqual(5, self._typical1_int.get(5))
        self.assertEqual(-2, self._typical1_int.get(6))

        # insert at back (append)
        self._typical1_int.insert(7, 102)

        # check follow-up state
        self.assertEqual(8, self._typical1_int.length())
        self.assertEqual(101, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))
        self.assertEqual(9, self._typical1_int.get(2))
        self.assertEqual(0, self._typical1_int.get(3))
        self.assertEqual(4, self._typical1_int.get(4))
        self.assertEqual(5, self._typical1_int.get(5))
        self.assertEqual(-2, self._typical1_int.get(6))
        self.assertEqual(102, self._typical1_int.get(7))

    def test_insert_typical1_errors(self):
        # index k must be in 0 - n inclusive
        with self.assertRaises(IndexError):
            self._typical1_int.set(-1, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(7, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(8, 99)

        with self.assertRaises(IndexError):
            self._typical1_int.set(100, 99)


    def test_insert_typical2(self):
        # test initial state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.insert(1, ('Chai Latte', 5.85))

        # test follow-up state
        self.assertEqual(4, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(1) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(2) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(3) )


        self._typical2_tuple.insert(3, ('Soy Chai Latte', 6.35))

        # test follow-up state
        self.assertEqual(5, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(1) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(2) )
        self.assertEqual( ('Soy Chai Latte', 6.35), self._typical2_tuple.get(3) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(4) )


    def test_insert_typical2_edgecases(self):
        # test initial state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self._typical2_tuple.insert(0, ('Chai Latte', 5.85))

        # test initial state
        self.assertEqual(4, self._typical2_tuple.length())
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(0) )
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(1) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(2) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(3) )

        self._typical2_tuple.insert(4, ('Soy Chai Latte', 6.35))

        # test initial state
        self.assertEqual(5, self._typical2_tuple.length())
        self.assertEqual( ('Chai Latte', 5.85), self._typical2_tuple.get(0) )
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(1) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(2) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(3) )
        self.assertEqual( ('Soy Chai Latte', 6.35), self._typical2_tuple.get(4) )


    def test_insert_typical2_error(self):
        # insert can occur at 0 <= k <= n
        with self.assertRaises(IndexError):
            self._typical2_tuple.insert(-1, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.insert(4, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.insert(5, ('Chai Latte', 5.85))

        with self.assertRaises(IndexError):
            self._typical2_tuple.insert(100, ('Chai Latte', 5.85))


    def test_insert_unusual1_empty(self):
        self.assertEqual(0, self._unusual1_empty.length())

        self._unusual1_empty.insert(0, 101)

        self.assertEqual(1, self._unusual1_empty.length())
        self.assertEqual( 101, self._unusual1_empty.get(0) )

        self._unusual1_empty.insert(1, 102)

        self.assertEqual(2, self._unusual1_empty.length())
        self.assertEqual( 101, self._unusual1_empty.get(0) )
        self.assertEqual( 102, self._unusual1_empty.get(1) )

        self._unusual1_empty.insert(1, 103)

        self.assertEqual(3, self._unusual1_empty.length())
        self.assertEqual( 101, self._unusual1_empty.get(0) )
        self.assertEqual( 103, self._unusual1_empty.get(1) )
        self.assertEqual( 102, self._unusual1_empty.get(2) )

    def test_insert_unusual1_empty_error(self):
        with self.assertRaises(IndexError):
            self._unusual1_empty.insert(-1, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.insert(1, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.insert(2, 99)

        with self.assertRaises(IndexError):
            self._unusual1_empty.insert(100, 99)


    def test_insert_unusual2_length1(self):
        # test initial state
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        self._unusual2_oneitem.insert(1, "twoitem")

        # test follow-up state
        self.assertEqual(2, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))
        self.assertEqual("twoitem", self._unusual2_oneitem.get(1))

        self._unusual2_oneitem.insert(0, "threeitem")

        # test follow-up state
        self.assertEqual(3, self._unusual2_oneitem.length())
        self.assertEqual("threeitem", self._unusual2_oneitem.get(0))
        self.assertEqual("oneitem", self._unusual2_oneitem.get(1))
        self.assertEqual("twoitem", self._unusual2_oneitem.get(2))



class TestLinkedListRemove(TestLinkedListBase):
    """ Tests for remove() """

    def test_remove_typical1(self):
        # check initial state
        self.assertEqual(6, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))

        self.assertEqual(0, self._typical1_int.remove(2))

        # check follow-up state
        self.assertEqual(5, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(4, self._typical1_int.get(2))
        self.assertEqual(5, self._typical1_int.get(3))
        self.assertEqual(-2, self._typical1_int.get(4))

        self.assertEqual(9, self._typical1_int.remove(1))

        # check follow-up state
        self.assertEqual(4, self._typical1_int.length())
        self.assertEqual(5, self._typical1_int.get(0))
        self.assertEqual(4, self._typical1_int.get(1))
        self.assertEqual(5, self._typical1_int.get(2))
        self.assertEqual(-2, self._typical1_int.get(3))

        self.assertEqual(5, self._typical1_int.remove(0))

        # check follow-up state
        self.assertEqual(3, self._typical1_int.length())
        self.assertEqual(4, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))
        self.assertEqual(-2, self._typical1_int.get(2))

        self.assertEqual(-2, self._typical1_int.remove(2))

        # check follow-up state
        self.assertEqual(2, self._typical1_int.length())
        self.assertEqual(4, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))

    def test_remove_typical1_error(self):
        with self.assertRaises(IndexError):
            self._typical1_int.remove(-1)
        with self.assertRaises(IndexError):
            self._typical1_int.remove(6)
        with self.assertRaises(IndexError):
            self._typical1_int.remove(7)
        with self.assertRaises(IndexError):
            self._typical1_int.remove(100)

    def test_remove_typical2(self):
        # test initial state
        self.assertEqual(3, self._typical2_tuple.length())
        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.get(0) )
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(1) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2) )

        self.assertEqual( ('Latte', 5.49), self._typical2_tuple.remove(0))

        # test follow-up state
        self.assertEqual(2, self._typical2_tuple.length())
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(0) )
        self.assertEqual( ('Caramel Frappuccino', 6.79), self._typical2_tuple.get(1) )

        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.remove(1))

        # test follow-up state
        self.assertEqual(1, self._typical2_tuple.length())
        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.get(0) )

        self.assertEqual( ('Drip Coffee', 2.19), self._typical2_tuple.remove(0))

        # test follow-up state
        self.assertEqual(0, self._typical2_tuple.length())

    def test_remove_typical2_error(self):
        with self.assertRaises(IndexError):
            self._typical2_tuple.remove(-1)

        with self.assertRaises(IndexError):
            self._typical2_tuple.remove(3)

        with self.assertRaises(IndexError):
            self._typical2_tuple.remove(4)

        with self.assertRaises(IndexError):
            self._typical2_tuple.remove(100)


    def test_remove_unusual1_empty(self):
        with self.assertRaises(IndexError):
            self._unusual1_empty.remove(-1)

        with self.assertRaises(IndexError):
            self._unusual1_empty.remove(0)

        with self.assertRaises(IndexError):
            self._unusual1_empty.remove(1)

        with self.assertRaises(IndexError):
            self._unusual1_empty.remove(100)

    def test_remove_unusual2_length1(self):
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        self.assertEqual("oneitem", self._unusual2_oneitem.remove(0))

        self.assertEqual(0, self._unusual2_oneitem.length())

    def test_remove_unusual2_length1_error(self):
        with self.assertRaises(IndexError):
            self._unusual2_oneitem.remove(-1)
        with self.assertRaises(IndexError):
            self._unusual2_oneitem.remove(1)
        with self.assertRaises(IndexError):
            self._unusual2_oneitem.remove(2)
        with self.assertRaises(IndexError):
            self._unusual2_oneitem.remove(100)


##############
#    Sort    #
##############

class TestLinkedListSort(TestLinkedListBase):
    """ Tests for the Sort functionality """

    def test_sort_typical_ascending(self):
        # input: 5,9,0,4,5,-2
        # expected output: -2,0,4,5,5,9

        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(5, self._typical1_int.get(0))  
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self._typical1_int.sort()
        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(-2, self._typical1_int.get(0))
        self.assertEqual(0, self._typical1_int.get(1))
        self.assertEqual(4, self._typical1_int.get(2))
        self.assertEqual(5, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(9, self._typical1_int.get(5))


    def test_sort_typical_descending(self):
        # input: 5,9,0,4,5,-2
        # expected output: 9,5,5,4,0,-2

        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(5, self._typical1_int.get(0))  
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self._typical1_int.sort(descending=True)
        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(9, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))
        self.assertEqual(5, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(0, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))


    def test_sort_typical_keymap1_ascending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Caramel Frappuccino', 6.79), ('Drip Coffee', 2.19), ('Latte', 5.49)
        
        self.assertEqual(3, self._typical2_tuple.length())  
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))
        
        # sort by name
        self._typical2_tuple.sort(map_to_key=lambda x : x[0])
        
        self.assertEqual(3, self._typical2_tuple.length())          
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(0))
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(2))  


    def test_sort_typical_keymap2_ascending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Drip Coffee', 2.19), ('Latte', 5.49), ('Caramel Frappuccino', 6.79)

        self.assertEqual(3, self._typical2_tuple.length())         
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

        # sort by price
        self._typical2_tuple.sort(map_to_key=lambda x : x[1])

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(0))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(1))  
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

    def test_sort_typical_keymap1_descending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))
        # sort by name
        self._typical2_tuple.sort(map_to_key=lambda x : x[0], descending=True)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))


    def test_sort_typical_keymap2_descending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Caramel Frappuccino', 6.79), ('Latte', 5.49), ('Drip Coffee', 2.19)
        
        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

        # sort by price
        self._typical2_tuple.sort(map_to_key=lambda x : x[1], descending=True)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(0))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(1))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(2))


    def test_sort_unusual1_empty(self):
        # input: <empty>
        # output: <empty> (no changes)
        self.assertEqual(0, self._unusual1_empty.length())
        self._unusual1_empty.sort()
        self.assertEqual(0, self._unusual1_empty.length())
        self._unusual1_empty.sort(descending=True)
        self.assertEqual(0, self._unusual1_empty.length())


    def test_sort_unusual2_onetime(self):
        # input: "oneitem"
        # output: "oneitem" (no changes)
        
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        # sort
        self._unusual2_oneitem.sort()

        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        # sort descending
        self._unusual2_oneitem.sort(descending=True)

        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))
        self.assertEqual(1, self._unusual2_oneitem.length())




    