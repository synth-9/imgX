import os
from PIL import Image
import piexif
import json

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
