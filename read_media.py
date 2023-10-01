"""
Purpose: Read media. Where media can be image or video.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def get_audio_addrs(dataset_path, audio_format):
    audio_addrs = []

    # Path to the folder where the images are stored

    # List all files in the folder
    files = os.listdir(dataset_path)

    # Run for all files in the folder
    for file in files:
        # Checks if the file has a tiff format
        audio_formats = [audio_format]
        if any(file.endswith(file_format) for file_format in audio_formats):
            audio_addrs.append(dataset_path+file)
    return audio_addrs
