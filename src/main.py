import os
import shutil
from textnode import TextNode, TextType


def copy_static(src_dir, dest_dir):
    """
    Recursively copy all contents from source directory to destination directory.
    First deletes all contents of destination directory for a clean copy.
    """
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        print(f"Deleting destination directory: {dest_dir}")
        shutil.rmtree(dest_dir)
    
    # Create destination directory
    print(f"Creating destination directory: {dest_dir}")
    os.mkdir(dest_dir)
    
    # Copy all contents recursively
    _copy_directory_contents(src_dir, dest_dir)


def _copy_directory_contents(src_dir, dest_dir):
    """
    Helper function to recursively copy directory contents.
    """
    if not os.path.exists(src_dir):
        print(f"Source directory does not exist: {src_dir}")
        return
    
    # List all items in source directory
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(src_path):
            # Copy file
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            # Create directory and copy contents recursively
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            _copy_directory_contents(src_path, dest_path)


def main():
    # Copy static files to public directory
    static_dir = "static"
    public_dir = "public"
    
    print("Starting static file copy...")
    copy_static(static_dir, public_dir)
    print("Static file copy completed!")


if __name__ == "__main__":
    main()
