from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.PLAINTEXT)
    delimited_bold: list[TextNode] = split_nodes_delimiter([text_node], "**", TextType.PLAINTEXT)
    delimited_bold_italic = split_nodes_delimiter(delimited_bold, "_", TextType.ITALIC)
    delimited_bold_italic_code = split_nodes_delimiter(delimited_bold_italic, "`", TextType.CODE)
    delimited_text_image = split_nodes_image(delimited_bold_italic_code)
    delimited_text_image_links = split_nodes_link(delimited_text_image)
    return delimited_text_image_links

def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:
    delimiters = ["**", "_", "`"]
    if delimiter not in delimiters:
        raise Exception("Delimiter not found - invalid Markdown")
    if delimiter == "**":
        new_text_type = TextType.BOLD
    elif delimiter == "_":
        new_text_type = TextType.ITALIC
    else:
        new_text_type = TextType.CODE
    output: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAINTEXT:
            output.append(node)
        else:
            new_nodes: list[str] = node.text.split(delimiter)
            text_output = []
            special_output = []
            for inner_node in new_nodes[1::2]:
                special_output.append(TextNode(inner_node, new_text_type))
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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    output = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        sample = node.text
        if images == []:
            output.append(node)
        else:
            for image in images:
                image_alt = image[0]
                image_link = image[1]
                pre, post = sample.split(f"![{image_alt}]({image_link})", 1)
                if pre != "":
                    output.append(TextNode(pre, TextType.PLAINTEXT))
                output.append(TextNode(image_alt, TextType.IMAGE, image_link))
                sample = post
            if sample != "":
                output.append(TextNode(sample, TextType.PLAINTEXT))
    return output





def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    output = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        sample = node.text
        if links == []:
            output.append(node)
        else:
            for link in links:
                link_alt = link[0]
                link_link = link[1]
                pre, post = sample.split(f"[{link_alt}]({link_link})", 1)
                output.append(TextNode(pre, TextType.PLAINTEXT))
                output.append(TextNode(link_alt, TextType.LINK, link_link))
                sample = post
            if sample != "":
                output.append(TextNode(sample, TextType.PLAINTEXT))
    return output
