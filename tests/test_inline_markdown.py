# test_textnode.py

import unittest

from  src.inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link
)
from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_image,
    text_type_link
)


class TestSplitNodeDelimeter(unittest.TestCase):

    def test_raises_exception(self) -> None:
        old_nodes: list = [TextNode("This is text with a **bolded word", text_type_text)]
        
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, "**", text_type_bold)

        self.assertTrue("Invalid markdown, formatted section not closed" in str(context.exception))

    def test_eq(self) -> None:
        old_nodes: list = [TextNode("This is text with a **bolded** word", "text")]
        new_nodes: list = split_nodes_delimiter(old_nodes, "**", text_type_bold)
        expected_new_nodes: list = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes, expected_new_nodes)


class TestSplitNodeImage(unittest.TestCase):

    def test_eq(self) -> None:
        old_nodes: list = [
            TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text
            )
        ]
        new_nodes: list = split_nodes_image(old_nodes)
        expected_new_nodes: list = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes, expected_new_nodes)


if __name__ == "__main__":
    unittest.main()
