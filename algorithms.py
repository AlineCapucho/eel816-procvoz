"""
Purpose: Store the algorithms used in the project.
"""

from pydub import AudioSegment
import os
import numpy as np

# Function to convert WAV file to MP3
def convert_to_mp3(wav_file):
    # Read the WAV file
    audio = AudioSegment.from_wav(wav_file)
    
    output_file = './results/' + wav_file.split("/")[2][:-4] + '.mp3'
    # Set the output format to MP3
    audio.export(output_file, format='mp3')
    print(f'Conversion to MP3 completed: {output_file}')

# Function to convert WAV file to FLAC
def convert_to_flac(wav_file):
    # Read the WAV file
    audio = AudioSegment.from_wav(wav_file)
    
    output_file = './results/' + wav_file.split("/")[2][:-4] + '.flac'
    # Set the output format to FLAC
    audio.export(output_file, format='flac')
    print(f'Conversion to FLAC completed: {output_file}')

# Function to convert WAV file to AAC
def convert_to_aac(wav_file):
    # Read the WAV file
    audio = AudioSegment.from_wav(wav_file)
    
    output_file = './results/' + wav_file.split("/")[2][:-4] + '.aac'
    # Set the output format to AAC
    # audio.export(output_file, format='aac')
    audio.export(output_file, format='adts')
    print(f'Conversion to AAC completed: {output_file}')

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