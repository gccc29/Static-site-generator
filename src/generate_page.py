from extract_title import extract_title
from md_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        _, ext = os.path.splitext(dir_path_content)
        ext = ext.lower()
        if ext == ".md":
            new_dest = dest_dir_path.replace(".md", ".html")
            generate_page(dir_path_content, template_path, new_dest, basepath)
    else:
        for item in os.listdir(dir_path_content):
            new_dir_path = os.path.join(dir_path_content, item)
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_dir_path, template_path, new_dest_path, basepath)





def generate_page(from_path, template_path, dest_path, basepath):

    # Print message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at 'from_path' and store the contents in a variable
    _, ext = os.path.splitext(from_path)
    ext = ext.lower()
    if ext == ".md":
        with open(from_path, "r") as f:
            markdown = f.read()
    else:
        raise Exception("from_path is not a .md file")

    # Read the template file at template_path and store the contents in a variable
    _, ext = os.path.splitext(template_path)
    ext = ext.lower()
    if ext == ".html":
        with open(template_path, "r") as f:
            template = f.read()
    else:
        raise Exception("template_path is not a .html file")

    # Use your 'markdown_to_html' func and '.to_html()' method to convert the markdown file to an HTML string
    html_nodes = markdown_to_html_node(markdown)
    for child in html_nodes.children:
        print(repr(child))
    html_str = html_nodes.to_html()

    # Use the 'extract_title' function to grab the title of the page
    title = extract_title(markdown)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated
    template_with_title = template.replace("{{ Title }}", title)
    template_with_content = template_with_title.replace("{{ Content }}", html_str)
    template_with_href = template_with_content.replace('href="/', f'href="{basepath}')
    final_html_str = template_with_href.replace('src="/', f'src="{basepath}')

    # Write the new full HTML page to a file at 'dest_path'.  Be sure to create any necessary directories if they don't exist
    # Make directories:
    parent_dir = os.path.dirname(dest_path)
    os.makedirs(parent_dir, exist_ok=True)
    # Write file:
    with open(dest_path, "w") as f:
        f.write(final_html_str)
