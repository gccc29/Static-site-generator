import shutil
import os
import sys
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from extract_title import extract_title
from md_to_html_node import markdown_to_html_node
from generate_page import generate_page, generate_pages_recursive


def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    # Copy files from /static to /public
    copied_files = copy_static_to("docs")
    print(f"Copied files: {copied_files}")

    # Generate a page from content/index.md using template.html as a template and write it to public/index.html
    generate_pages_recursive("content", "template.html", "docs", basepath)

def copy_static_to(to_path: str, from_path: str = "static"):
    #delete contents of public
    if os.path.exists(to_path):
        files_to_delete = os.listdir(to_path)
        print(f"Deleted files: {files_to_delete}")
        shutil.rmtree(to_path)
    else:
        print("Nothing to delete")
    os.mkdir(os.path.join(".", to_path))

    return copy_directory(from_path, to_path)

def copy_directory(from_path, to_path):
    # recursive function to copy contents from static
    copied = []
    contents = os.listdir(from_path)
    for item in contents:
        source = os.path.join(from_path, item)
        destination = os.path.join(to_path, item)

        if os.path.isfile(source):
            copied.append(f"file: {item}")
            shutil.copy(source, destination)
        else:
            os.mkdir(destination)
            copied.append(f"dir: {item}")
            copied.extend(copy_directory(source, destination))

    return copied


if __name__ == "__main__":
    main()
