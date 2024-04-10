# test_textnode.py

import unittest

from  src.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is an italic text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a bold text node", "bold")
        self.assertTrue(node.url == None)


if __name__ == "__main__":
    unittest.main()
