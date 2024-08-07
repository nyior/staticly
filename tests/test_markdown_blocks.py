import unittest
from src.htmlnode import ParentNode
from src.markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)


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

    def test_markdown_to_blocks_newlines(self) -> None:
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

    def test_block_to_block_types(self) -> None:
        block: str = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block: str = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block: str = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block: str = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block: str = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block: str = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    
    def test_paragraph(self) -> None:
        md: str = """
This is **bolded** paragraph
text in a p
tag here

"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self) -> None:
        md: str = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self) -> None:
        md: str = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self) -> None:
        md: str = """
# this is an h1

this is paragraph text

## this is an h2
"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self) -> None:
        md: str = """
> This is a
> blockquote block

this is paragraph text

"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self) -> None:
        md: str = """
> This is a
> blockquote block

this is paragraph text

"""
        node: ParentNode = markdown_to_html_node(md)
        html: ParentNode = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()