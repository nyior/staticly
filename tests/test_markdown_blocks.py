import unittest
from src.markdown_blocks import markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self) -> None:
        md: str = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks: list = markdown_to_blocks(md)
        print(f"\n{blocks}\n")
        expected_blocks: list = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(len(blocks), len(expected_blocks))
        self.assertEqual(
            blocks,
            expected_blocks
        )

    def test_markdown_to_blocks_newlines(self):
        md: str = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        blocks: list = markdown_to_blocks(md)
        expected_blocks: list = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(len(blocks), len(expected_blocks))
        self.assertEqual(
            blocks,
            expected_blocks
        )


if __name__ == "__main__":
    unittest.main()