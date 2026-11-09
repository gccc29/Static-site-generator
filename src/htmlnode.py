
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
