from tree import Bintree
import unittest


class BintreeTest(unittest.TestCase):
    def setUp(self):
        self.b = Bintree()

    def testInsert(self):
        self.b.store('r', 10)
        self.assertEqual(self.b.root.key, 'r', "Root store unsuccessful")
        self.assertEqual(self.b.root.val, 10, "Root store unsuccessful")

    def testInsertMore(self):
        self.b.store('r', 10)
        self.b.store('b', 15)

        self.assertEqual(self.b.root.left.key, 'b', "Store unsuccessful")
        self.assertEqual(self.b.root.left.val, 15, "Store unsuccessful")

    def testSearchKeyError(self):
        with self.assertRaises(KeyError):
            self.b.search("e")

    def testSearch(self):
        self.b.store('r', 10)
        self.b.store('c', 18)
        node = self.b.search('c')
        self.assertEqual(
            node.key, 'c', "The bintree does not have the element with key")

    def testContainsTrue(self):
        self.b.store('r', 10)
        self.b.store('c', 18)
        self.assertTrue(self.b.__contains__(
            'c'), "The bintree does contain key")

    def testContainsFalse(self):
        self.b.store('r', 10)
        self.b.store('c', 18)
        self.assertFalse(self.b.__contains__(
            'e'), "The bintree does not contain key")

    def testWrite(self):
        self.b.store('r', 10)
        self.b.store('b', 15)
        self.b.store('c', 5)
        self.b.store('m', 8)
        self.b.store('t', 7)
        self.b.store('h', 4)
        self.b.store('g', 9)

        self.b.write()


if __name__ == '__main__':
    unittest.main()
