# main.py

from textnode import TextNode

def main() -> None:
    textnode = TextNode(
        text="Sample text node", text_type="bold", url="sample url"
    )
    print(textnode)


main()   