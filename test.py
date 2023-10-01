"""
Purpose: Test code.
"""

from pydub import AudioSegment
import os

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

# Path to your WAV file
input_wav = './data/jurcic-001-120912_124317_0001940_0002325.wav'

# Convert WAV to MP3
convert_to_mp3(input_wav)

# Convert WAV to FLAC
convert_to_flac(input_wav)

# Convert WAV to AAC
convert_to_aac(input_wav)