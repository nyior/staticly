# textnode.py


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