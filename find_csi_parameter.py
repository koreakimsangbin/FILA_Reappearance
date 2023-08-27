import numpy as np
def csi_value(file_path):
    with open(file_path, 'rb') as f:
        csi_binary = f.read()
    csi_data = np.frombuffer(csi_binary, dtype=np.complex64).copy()

    return csi_data


def extract_parameters(csi_values, central_frequency=2.45e9, bandwidth=20e6):
    amplitudes = np.abs(csi_values)

    if bandwidth == 20e6:
        subcarrier_spacing = bandwidth / 60
    else:
        subcarrier_spacing = bandwidth / 120

    half_bandwidth = bandwidth / 2
    half_subcarrier_spacing = subcarrier_spacing / 2

    num_sub_carriers = len(csi_values)
    frequencies = np.abs(central_frequency - half_bandwidth + half_subcarrier_spacing +
                         np.arange(num_sub_carriers) * subcarrier_spacing)

    return frequencies, amplitudes, central_frequency
