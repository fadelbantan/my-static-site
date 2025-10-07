from enum import Enum
from htmlnode import LeafNode

# Enumaration for the differnet text types
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Equality check for testing purposes
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    # String representation for debugging
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if TextType.TEXT == text_node.text_type:
        return LeafNode(None, text_node.text)
    if TextType.BOLD == text_node.text_type:
        return LeafNode("b", text_node.text)
    if TextType.ITALIC == text_node.text_type:
        return LeafNode("i", text_node.text)
    if TextType.CODE == text_node.text_type:
        return LeafNode("code", text_node.text)
    if TextType.LINK == text_node.text_type:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if TextType.IMAGE == text_node.text_type:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
