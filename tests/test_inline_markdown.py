# test_textnode.py

import unittest

from  src.inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)
from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_image,
    text_type_link,
    text_type_code,
    text_type_italic
)


class TestSplitNodeDelimeter(unittest.TestCase):

    def test_raises_exception(self) -> None:
        old_nodes: list = [TextNode("This is text with a **bolded word", text_type_text)]
        
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, "**", text_type_bold)

        self.assertTrue("Invalid markdown, formatted section not closed" in str(context.exception))

    def test_image_eq(self) -> None:
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


class TestSplitNodeLink(unittest.TestCase):

    def test_link_eq(self) -> None:
        old_nodes: list = [
            TextNode(
                "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text
            )
        ]
        new_nodes: list = split_nodes_link(old_nodes)
        expected_new_nodes: list = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes, expected_new_nodes)


class TextToTextnodes(unittest.TestCase):

    def test_eq(self) -> None:
        text: str = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes: list = text_to_textnodes(text)
        expected_nodes: list = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]

        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
