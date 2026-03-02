import os
import shutil

from textnode import TextNode
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def clear_public_folder():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

def copy_files_to_public(source, dest):
    print("Populating public directory")
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(dest, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_to_public(from_path, dest_path)

def gen_page():
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

def main():
    clear_public_folder()
    copy_files_to_public(dir_path_static, dir_path_public)
    gen_page()

if __name__ == "__main__":
    main()
