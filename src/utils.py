import re


def extract_markdown_images(text: str) -> list:
    images: list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


def extract_markdown_links(text: str) -> list:
    links: list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links