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
            for attr, value in self.props.items():
                attrs += f' {attr}="{value}"'
   
        return attrs


class LeafNode(HTMLNode):

    def __init__(
        self, 
        value: str,
        tag: str = None, 
        props: dict[str, str] = None,
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return f"{self.value}"
        
        props: str = self.props_to_html()
        
        leaf_node: str = f"<{self.tag}{props}>{self.value}<{self.tag}>"
        return leaf_node