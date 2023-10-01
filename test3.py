"""
Purpose: Test code.
"""

import os
import numpy as np
import soundfile as sf

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

audio1_path = 'results/jurcic-001-120912_124317_0001940_0002325.flac'
audio2_path = 'results/jurcic-001-120912_124317_0001940_0002325.mp3'

# Carrega os arquivos de áudio
audio1, sr1 = sf.read(audio1_path)
audio2, sr2 = sf.read(audio2_path)

# Calcula as medidas de erro
rmse = calculate_rmse(audio1, audio2)
psnr = calculate_psnr(audio1, audio2)
compression_rate = calculate_compression_rate(audio1_path, audio2_path)

# Imprime os resultados
print('Root Mean Square Error:', rmse)
print('Peak Signal Noise Ratio:', psnr)
print('Compression Rate:', compression_rate)