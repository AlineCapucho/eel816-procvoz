"""
Purpose: Test code.
"""

import os
import numpy as np

def get_audio_addrs(dataset_path):
    audio_addrs = []

    # Path to the folder where the images are stored

    # List all files in the folder
    files = os.listdir(dataset_path)

    # Run for all files in the folder
    for file in files:
        # Checks if the file has a tiff format
        audio_formats = ['.wav']
        if any(file.endswith(file_format) for file_format in audio_formats):
            audio_addrs.append(dataset_path+file)
    return audio_addrs

print(get_audio_addrs("./data/"))