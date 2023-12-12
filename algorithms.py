"""
Purpose: Store the algorithms used in the project.
"""

from pydub import AudioSegment
import os
import numpy as np

# Get file extension
def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    
    return extension[1:]

# Function to convert audio file to MP3
def convert_to_mp3(file_path, output_file = ''):
    format = get_file_extension(file_path)

    # Read the file
    audio = AudioSegment.from_file(file_path, format)

    if (not output_file):
        output_file = './results/' + file_path.split("/")[2][:-4] + '.mp3'
    else:
        if (output_file[-4:] != '.mp3'):
            output_file += '.mp3'

    # Set the output format to MP3
    audio.export(output_file, format='mp3')
    print(f'Conversion to MP3 completed: {output_file}')

# Function to convert audio file to FLAC
def convert_to_flac(file_path, output_file = ''):
    format = get_file_extension(file_path)

    # Read the file
    audio = AudioSegment.from_file(file_path, format)
    
    if (not output_file):
        output_file = './results/' + file_path.split("/")[2][:-4] + '.flac'
    else:
        if (output_file[-5:] != '.flac'):
            output_file += '.flac'
    
    # Set the output format to FLAC
    audio.export(output_file, format='flac')
    print(f'Conversion to FLAC completed: {output_file}')

# Function to convert audio file to AAC
def convert_to_aac(file_path, output_file = ''):
    format = get_file_extension(file_path)

    # Read the file
    audio = AudioSegment.from_file(file_path, format)
    
    if (not output_file):
        output_file = './results/' + file_path.split("/")[2][:-4] + '.aac'
    else:
        if (output_file[-4:] != '.aac'):
            output_file += '.aac'
    
    # Set the output format to AAC
    # audio.export(output_file, format='aac')
    audio.export(output_file, format='adts')
    print(f'Conversion to AAC completed: {output_file}')

# Function to audio file to WAV
def convert_to_wav(file_path, output_file = ''):
    format = get_file_extension(file_path)

    # Read the file
    audio = AudioSegment.from_file(file_path, format)
    
    if (not output_file):
        output_file = './results/' + file_path.split("/")[2][:-4] + '.wav'
    else:
        if (output_file[-4:] != '.wav'):
            output_file += '.wav'
    
    audio.export(output_file, format='wav')
    print(f'Conversion to WAV completed: {output_file}')

def calculate_rmse(audio1, audio2):
    mse = np.mean((audio1 - audio2) ** 2)
    rmse = np.sqrt(mse)
    return rmse

def calculate_psnr(audio1, audio2):
    max_value = 2**16 - 1  # Valor máximo para uma amostra de áudio de 16 bits
    mse = np.mean((audio1 - audio2) ** 2)
    psnr = 10 * np.log10((max_value ** 2) / mse)
    return psnr

def calculate_compression_rate(file1, file2):
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)
    rate = size2 / size1
    return rate