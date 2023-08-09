import numpy as np


def csi_value(file_path):
    with open(file_path, 'rb') as f:
        csi_binary = f.read()
    csi_data = np.frombuffer(csi_binary, dtype=np.complex64).copy()

    return csi_data


def extract_parameters(csi_values, central_frequency=24e8, subcarrier_spacing=20e6):
    amplitudes = np.abs(csi_values)

    num_sub_carriers = len(csi_values)
    frequencies = np.abs(central_frequency + (np.arange(num_sub_carriers) - num_sub_carriers // 2) * subcarrier_spacing)
    return frequencies, amplitudes, central_frequency
