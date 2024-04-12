# htmlnode.py

class HTMLNode:

    def __init__(
        self, 
        tag: str=None, 
        value: str=None, 
        children: list[object]=None, 
        props: dict[str, str]=None
    ) -> None:
        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, { self.props})"

    def props_to_html(self) -> str:
        attrs: str = ""
        if self.props is not None:
            for attr, value in self.props.values():
                attrs += f" {attr}=\"{value}\" "
