# test_utils.py

import unittest

from src.utils import (
    extract_markdown_links, 
    extract_markdown_images
)


class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self) -> None:
        text: str = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images: list = extract_markdown_images(text)
        self.assertEqual(
            images,
            [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        )

    def test_extract_markdown_links(self) -> None:
        text: str = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links: list = extract_markdown_links(text)
        self.assertEqual(
            links,
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )


if __name__ == "__main__":
    unittest.main()
