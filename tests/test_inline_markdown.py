# test_textnode.py

import unittest

from  src.inline_markdown import split_nodes_delimiter
from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
)


class TestInlineMarkdown(unittest.TestCase):

    def test_raises_exception(self) -> None:
        old_nodes: list = [TextNode("This is text with a **bolded word", "text")]
        
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


if __name__ == "__main__":
    unittest.main()
