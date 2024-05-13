# main.py

from textnode import TextNode


def main() -> None:
    textnode = TextNode(
        text="Sample text node", text_type="bold", url="sample url"
    )
    print(textnode)


if __name__ == "__main__":
    main()   