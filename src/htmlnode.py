
class HTMLNode:
    def __init__(
        self, tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        output = ""
        for key, value in self.props.items():
            output += f' {key}="{value}"'
        return output

    def __repr__(self):
        if self.children == None or self.children == []:
            chdn = "no children"
        else:
            chdn = ""
            for child in self.children:
                chdn += f"{child.tag} "
        if self.props == None or self.props == {}:
            prps = "no props"
        else:
            prps = ""
            for key, value in self.props.items():
                prps += f"({key}: {value})"
        return f"HTML Node(Tag: {self.tag}, value: {self.value}, children: {chdn}, props: {prps})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        if self.tag == None or self.tag == "":
            return f"{self.value}"
        else:
            if self.props:
                for key, value in self.props.items():
                    return f'<{self.tag} {key}="{value}">{self.value}</{self.tag}>'
            return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        if self.props == None or self.props == {}:
            prps = "no props"
        else:
            prps = ""
            for key, value in self.props.items():
                prps += f"({key}: {value})"
        return f"Leaf Node(Tag: {self.tag}, value: {self.value}, props: {prps})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children, props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("No tag - tag required")
        if self.children == None or self.children == []:
            raise ValueError("No children - children required")
        text = ""
        for child in self.children:
            text += child.to_html()
        return f'<{self.tag}>{text}</{self.tag}>'
