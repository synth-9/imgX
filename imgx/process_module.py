import os
from PIL import Image
import piexif
import json
import shutil
import random
from pathlib import Path

class ProcessModule:
    def __init__(self, path=None, destination=None):
        self.path = path if path else os.getcwd()
        self.destination = destination if destination else os.getcwd()

    def read_metadata_and_write_to_file(self):
        """
        Read metadata from images in the path and write details to a file in the destination.
        """
        metadata_file_path = os.path.join(self.destination, 'image_metadata.json')
        image_files = [f for f in os.listdir(self.path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

        metadata_list = []

        for image_file in image_files:
            image_path = os.path.join(self.path, image_file)
            with Image.open(image_path) as img:
                size_in_bytes = os.path.getsize(image_path)
                size_in_mb = size_in_bytes / (1024 * 1024)
                metadata = {
                    "image_name": image_file,
                    "size_MB": round(size_in_mb, 2),
                    "size_B": size_in_bytes,
                    "path": image_path,
                    "location": self.get_location(img)
                }
                metadata_list.append(metadata)

        with open(metadata_file_path, 'w') as f:
            json.dump(metadata_list, f, indent=4)

        print(f"Metadata written to {metadata_file_path}")

    def get_location(self, image):
        """
        Extract location (if available) from image EXIF data.
        """
        try:
            exif_data = piexif.load(image.info['exif'])
            gps_info = exif_data.get('GPS')
            if gps_info:
                return str(gps_info)
            else:
                return "Location Not Available"
        except KeyError:
            return "No EXIF Data"

    def flatten_directory(self):
        """
        Flatten one level of subdirectories in the given parent directory by moving all image files
        from the subdirectories to the parent directory. If a filename conflict occurs, append a
        random sequence of numbers to the filename.
        """
        parent_dir = self.path
        
        # Define allowed image extensions
        image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

        # Traverse through each item in the parent directory
        for item in os.listdir(parent_dir):
            sub_dir = os.path.join(parent_dir, item)
            # Check if the item is a directory
            if os.path.isdir(sub_dir):
                # List all files in the subdirectory
                for file_name in os.listdir(sub_dir):
                    file_path = os.path.join(sub_dir, file_name)
                    # Check if the file is an image and not a hidden file
                    if not file_name.startswith('._') and Path(file_path).suffix.lower() in image_extensions:
                        if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
                            new_file_path = os.path.join(parent_dir, file_name)
                            # Resolve conflicts if the file already exists in the parent directory
                            while os.path.exists(new_file_path):
                                # Generate a random number to append to the file name
                                rand_num = random.randint(10000, 99999)
                                new_file_name = f"{Path(file_name).stem}_{rand_num}{Path(file_name).suffix}"
                                new_file_path = os.path.join(parent_dir, new_file_name)
                            # Move the file to the parent directory
                            try:
                                shutil.move(file_path, new_file_path)
                                print(f"Moved '{file_name}' to '{new_file_path}'")
                            except Exception as e:
                                print(f"Failed to move '{file_name}': {e}")
                        else:
                            print(f"Skipping '{file_name}': Unable to access file")

                # Optionally, remove the directory if it's empty after moving the files
                if not os.listdir(sub_dir):
                    try:
                        os.rmdir(sub_dir)
                    except OSError as e:
                        print(f"Failed to remove directory '{sub_dir}': {e}")

        print(f"Flattening complete for directory: {parent_dir}")