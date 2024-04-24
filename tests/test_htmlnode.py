# test_textnode.py

import unittest

from  src.htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self) -> None:
        node = HTMLNode(
            tag="a", 
            value="link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )

        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self) -> None:
        leaf = LeafNode(
            tag="a", 
            value="link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        leaf2 = LeafNode(
            tag="p", 
            value="a paragraph", 
        )
        
        self.assertEqual(
            leaf.to_html(), 
            '<a href="https://www.google.com" target="_blank">link<a>'
        )
        self.assertEqual(
            leaf2.to_html(), 
            '<p>a paragraph<p>'
        )
    
    def test_raises_exception(self) -> None:
        leaf = LeafNode(
            tag="a", 
            value=None,
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        with self.assertRaises(ValueError) as context:
            print(context)
            leaf.to_html()

        self.assertTrue("You must pass a value" in str(context.exception))
    
    def test_returns_raw_value(self) -> None:
        leaf = LeafNode(
            value="this is a link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            leaf.to_html(), 
            "this is a link"
        )


if __name__ == "__main__":
    unittest.main()