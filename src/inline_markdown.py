from src.textnode import (
    TextNode,
    text_type_text,
)


# TODO: Extend function to support multiple levels of nesting
# E.g: This is an *italic and **bold** word*.
def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list:
    new_nodes: list = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes: list = []
        sections: list = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes