# test_textnode.py

import unittest

from  src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", 
            value="link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )

        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
        )

if __name__ == "__main__":
    unittest.main()
