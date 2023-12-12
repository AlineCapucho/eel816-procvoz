"""
Purpose: Execute the objetive of the project.
"""

import numpy as np
import pandas as pd

from read_media import get_audio_addrs
from algorithms import convert_to_mp3, convert_to_flac, convert_to_aac
from algorithms import calculate_rmse, calculate_psnr, calculate_compression_rate

import soundfile as sf
from pydub import AudioSegment
import time

id_vals = []
rmse_vals = []
psnr_vals = []
cr_vals = []
time_vals = []
format_vals = []

def add_data(id_val, format_val, rmse_val, psnr_val, cr_val):
    id_vals.append(id_val)
    format_vals.append(format_val)
    rmse_vals.append(rmse_val)
    psnr_vals.append(psnr_val)
    cr_vals.append(cr_val)

def read_aac_file(aac_file):
    audio = AudioSegment.from_file(aac_file, format="aac")
    array_audio = audio.get_array_of_samples()
    return np.array(array_audio)

# Prepare path to each wav file
dataset_path = "./data/"
results_path = "./results/"
wav_files = get_audio_addrs(dataset_path, '.wav')

# Apply each compression algorithm to each audio file
for wav_file in wav_files:
    start_time = time.time()
    convert_to_mp3(wav_file)
    execution_time = time.time() - start_time
    time_vals.append(execution_time)

    start_time = time.time()
    convert_to_flac(wav_file)
    execution_time = time.time() - start_time
    time_vals.append(execution_time)

    start_time = time.time()
    convert_to_aac(wav_file)
    execution_time = time.time() - start_time
    time_vals.append(execution_time)


# Prepare path to each mp3, flac, aac file
mp3_files = get_audio_addrs(results_path, '.mp3')
flac_files = get_audio_addrs(results_path, '.flac')
aac_files = get_audio_addrs(results_path, '.aac')

# Compute measure RMSE, PSNR and CR
for i in range(len(wav_files)):
    # Load audio file
    audio1, sr1 = sf.read(wav_files[i])
    audio2, sr2 = sf.read(mp3_files[i])
    audio3, sr3 = sf.read(flac_files[i])
    # audio4, sr4 = sf.read(aac_files[i])
    audio4 = read_aac_file(aac_files[i])

    # Calculate error measure for mp3 file
    rmse = calculate_rmse(audio1, audio2)
    psnr = calculate_psnr(audio1, audio2)
    compression_rate = calculate_compression_rate(wav_files[i], mp3_files[i])

    # Print result for mp3 file
    print('Root Mean Square Error:', rmse)
    print('Peak Signal Noise Ratio:', psnr)
    print('Compression Rate:', compression_rate)
    add_data(i, "mp3", rmse, psnr, compression_rate)

    # Calculate error measure for flac file
    rmse = calculate_rmse(audio1, audio3)
    psnr = calculate_psnr(audio1, audio3)
    compression_rate = calculate_compression_rate(wav_files[i], flac_files[i])

    # Print result for flac file
    print('Root Mean Square Error:', rmse)
    print('Peak Signal Noise Ratio:', psnr)
    print('Compression Rate:', compression_rate)
    add_data(i, "flac", rmse, psnr, compression_rate)

    # Calculate error measure for aac file
    diff = len(audio4) - len(audio1)
    rmse = calculate_rmse(audio1, audio4[diff:])
    psnr = calculate_psnr(audio1, audio4[diff:])
    compression_rate = calculate_compression_rate(wav_files[i], aac_files[i])

    # Print result for aac file
    print('Root Mean Square Error:', rmse)
    print('Peak Signal Noise Ratio:', psnr)
    print('Compression Rate:', compression_rate)
    add_data(i, "aac", rmse, psnr, compression_rate)

df = pd.DataFrame({'id': id_vals, 'format': format_vals, 'rmse': rmse_vals, 'psnr': psnr_vals, 'compression_rate': cr_vals, 'runtime': time_vals})
df.to_csv("./csv_results/results_dataframe.csv", index=False)