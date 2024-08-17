# textnode.py
from htmlnode import LeafNode


text_type_text: str = "text"
text_type_bold: str = "bold"
text_type_italic: str = "italic"
text_type_code: str = "code"
text_type_link: str = "link"
text_type_image: str = "image"


class TextNode:
    
    def __init__(
        self, text: str, text_type: str, url: str = None
    ) -> None:
        self.text = text 
        self.text_type = text_type 
        self.url = url
    
    def __eq__(self, textnode: object) -> bool:
        return(
            self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text)
    
    if text_node.text_type == text_type_bold:
        return LeafNode(value=text_node.text, tag="b")
    
    if text_node.text_type == text_type_italic:
        return LeafNode(value=text_node.text, tag="i")
    
    if text_node.text_type == text_type_code:
        return LeafNode(value=text_node.text, tag="code")
    
    if text_node.text_type == text_type_link:
        props: dict = {"href": text_node.url, "target": "_blank"}
        return LeafNode(value=text_node.text, tag="a", props=props)
    
    if text_node.text_type == text_type_image:
        props: dict = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(value="", tag="img", props=props)

    raise ValueError("Incorrect node type")