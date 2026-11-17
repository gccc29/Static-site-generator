from blocks import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_blocks import markdown_to_blocks
from split_nodes import text_to_textnodes
from textnode import TextNode, text_node_to_html_node ,TextType
import re

def markdown_to_html_node(markdown: str) -> ParentNode:

    # Split the markdown string into blocks
    md_blocks = markdown_to_blocks(markdown)

    # Loop over each block to:
        # 1. Determine the block type
        # 2. Based on block type, create a new HTMLNode with the proper data
        # 3. Assign proper child HTMLNode objects to the block node
        # 4. Handle code blocks separately (should not do any inline md passing of its chilrdren)

    output = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                output.append(paragraph_block_to_HTMLnode(block))
            case BlockType.HEADING:
                output.append(heading_to_HTMLnode(block))
            case BlockType.CODE:
                output.append(code_to_HTML_node(block))
            case BlockType.QUOTE:
                output.append(quote_to_HTMLnode(block))
            case BlockType.UNORDERED_LIST:
                output.append(unordered_list_to_HTML_node(block))
            case BlockType.ORDERED_LIST:
                output.append(ordered_list_to_HTML_node(block))

    return ParentNode("div", output)

# Make all the block nodes children under a single parent HTMLNode (just a <div>) and return it

# Helper functions:
def paragraph_block_to_HTMLnode(block: str) -> ParentNode:
    stripped_block = block.replace("\n", " ")
    text_nodes = text_to_textnodes(stripped_block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("p", html_nodes)

def heading_to_HTMLnode(block: str) -> ParentNode:
    clean_line = block.lstrip()
    hash_count = len(clean_line) - len(clean_line.lstrip("#"))
    heading_text = block.strip("# ")
    text_nodes = text_to_textnodes(heading_text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode(f"h{hash_count}", html_nodes)

def code_to_HTML_node(block: str) -> ParentNode:
    stripped_block = (block.strip("` ")).lstrip("\n")

    txt_node = TextNode(stripped_block, TextType.CODE)
    html_node = text_node_to_html_node(txt_node)
    return ParentNode("pre", [html_node])

def quote_to_HTMLnode(block: str) -> ParentNode:
    stripped_block = block.strip("> ")
    text_nodes = text_to_textnodes(stripped_block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("blockquote", html_nodes)

def unordered_list_to_HTML_node(block: str) -> ParentNode:
    items = block.split("\n")
    output_nodes = []
    for item in items:
        stripped_item = item.strip("- ")
        text_nodes = text_to_textnodes(stripped_item)
        html_nodes = []
        for node in text_nodes:
            html_nodes.append(text_node_to_html_node(node))
        output_nodes.append(ParentNode("li", html_nodes))
    return ParentNode("ul", output_nodes)

def ordered_list_to_HTML_node(block: str) -> ParentNode:
    items = block.split("\n")
    output_nodes = []
    for item in items:
        stripped_item = re.sub(r"^\d+\.\s*", "", item)
        text_nodes = text_to_textnodes(stripped_item)
        html_nodes = []
        for node in text_nodes:
            html_nodes.append(text_node_to_html_node(node))
        output_nodes.append(ParentNode("li", html_nodes))
    return ParentNode("ol", output_nodes)
