# test_textnode.py

import unittest

from  src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode, text_node_to_html_node


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
            '<a href="https://www.google.com" target="_blank">link</a>'
        )
        self.assertEqual(
            leaf2.to_html(), 
            '<p>a paragraph</p>'
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
    
    def test_textnode_to_html_node(self) -> None:
        textnode = TextNode("This is text node", "text")
        leafnode = text_node_to_html_node(textnode)

        self.assertTrue(isinstance(leafnode, LeafNode))


class TestParentNode(unittest.TestCase):
    def test_to_html(self) -> None:
        node = ParentNode(
            "a",
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(value="Normal text"),
            ],
        )
        
        self.assertEqual(
            node.to_html(), 
            "<a><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>"
        )
    
    def test_nested_to_html(self) -> None:
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "a",
                    [
                        LeafNode(tag="b", value="Bold text"),
                        LeafNode(tag="i", value="italic text")
                    ],
                ),
                ParentNode(
                    "a",
                    [
                        LeafNode(tag="b", value="Bold text")
                    ],
                ),
            ],
        )
        
        self.assertEqual(
            node.to_html(), 
            "<p><a><b>Bold text</b><i>italic text</i></a><a><b>Bold text</b></a></p>"
        )
       
    
    def test_raises_exception_for_none_tag(self) -> None:
        leaf = ParentNode( 
            tag=None,
            children=[]
        )
        with self.assertRaises(ValueError) as context:
            print(context)
            leaf.to_html()

        self.assertTrue("A tag must be provided" in str(context.exception))
    
    def test_raises_exception_for_none_children(self) -> None:
        leaf = ParentNode( 
            tag="p",
            children=None
        )
        with self.assertRaises(ValueError) as context:
            print(context)
            leaf.to_html()

        self.assertTrue("This node must have children" in str(context.exception))
    

if __name__ == "__main__":
    unittest.main()