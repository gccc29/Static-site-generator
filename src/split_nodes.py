from textnode import TextNode, TextType

def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:
    delimiters = ["**", "_", "`"]
    output: list[TextNode] = []
    if delimiter not in delimiters:
        raise Exception("Delimiter not found - invalid Markdown")
    for node in old_nodes:
        if node.text_type != TextType.PLAINTEXT:
            output.append(node)
        else:
            new_nodes: list[str] = node.text.split(delimiter)
            text_output = []
            special_output = []
            for inner_node in new_nodes[1::2]:
                special_output.append(TextNode(inner_node, text_type))
            for inner_node in new_nodes[0::2]:
                text_output.append(TextNode(inner_node, TextType.PLAINTEXT))
            if len(special_output) != len(text_output)-1:
                raise Exception("Missing a delimiter")
            for i in range (len(special_output)):
                output.append(text_output[i])
                output.append(special_output[i])
            output.append(text_output[-1])

    for output_node in output:
        if output_node.text == "":
            output.remove(output_node)
    return output
