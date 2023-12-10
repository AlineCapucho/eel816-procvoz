"""
Purpose: Execute the objetive of the project.
"""

import pandas as pd

from read_media import get_audio_addrs
from algorithms import convert_to_mp3, convert_to_flac, convert_to_aac
from algorithms import calculate_rmse, calculate_psnr, calculate_compression_rate

import soundfile as sf

id_vals = []
rmse_vals = []
psnr_vals = []
cr_vals = []

def add_data(id_val, rmse_val, psnr_val, cr_val):
    id_vals.append(id_val)
    rmse_vals.append(rmse_val)
    psnr_vals.append(psnr_val)
    cr_vals.append(cr_val)

# Prepare path to each wav file
dataset_path = "./data/"
results_path = "./results/"
wav_files = get_audio_addrs(dataset_path, '.wav')

# Apply each compression algorithm to each audio file
for wav_file in wav_files:
    convert_to_mp3(wav_file)
    convert_to_flac(wav_file)
    convert_to_aac(wav_file)

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

    # Calculate error measure for mp3 file
    rmse = calculate_rmse(audio1, audio2)
    psnr = calculate_psnr(audio1, audio2)
    compression_rate = calculate_compression_rate(wav_files[i], mp3_files[i])

    # Print result for mp3 file
    print('Root Mean Square Error:', rmse)
    print('Peak Signal Noise Ratio:', psnr)
    print('Compression Rate:', compression_rate)
    add_data(i, rmse, psnr, compression_rate)

    # Calculate error measure for flac file
    rmse = calculate_rmse(audio1, audio3)
    psnr = calculate_psnr(audio1, audio3)
    compression_rate = calculate_compression_rate(wav_files[i], flac_files[i])

    # Print result for flac file
    print('Root Mean Square Error:', rmse)
    print('Peak Signal Noise Ratio:', psnr)
    print('Compression Rate:', compression_rate)
    add_data(i, rmse, psnr, compression_rate)

    # # Calculate error measure for aac file
    # rmse = calculate_rmse(audio1, audio4)
    # psnr = calculate_psnr(audio1, audio4)
    # compression_rate = calculate_compression_rate(wav_files[i], aac_files[i])

    # # Print result for aac file
    # print('Root Mean Square Error:', rmse)
    # print('Peak Signal Noise Ratio:', psnr)
    # print('Compression Rate:', compression_rate)
    # add_data(i, rmse, psnr, compression_rate)

df = pd.DataFrame({'id': id_vals, 'rmse': rmse_vals, 'psnr': psnr_vals, 'compression_rate': cr_vals})
df.to_csv("./csv_results/results_dataframe.csv", index=False)