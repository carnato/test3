import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory by their file extensions.
    Files will be moved into folders named after their extensions.

    Args:
        directory (str): The path to the directory to organize.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Create a folder for the extension if it doesn't exist
        folder_name = file_extension[1:] if file_extension else "no_extension"
        folder_path = os.path.join(directory, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        # Move the file into the corresponding folder
        shutil.move(file_path, os.path.join(folder_path, filename))

    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)
