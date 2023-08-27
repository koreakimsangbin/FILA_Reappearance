import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import ifft
from truncation_window import *
import math
def get_time_domain(file_path):
    with open(file_path, 'rb') as f:
        csi_binary = f.read()

    arr_num_car = []
    remainder = len(csi_binary) % 8
    if remainder != 0:
        csi_binary = csi_binary[:-(len(csi_binary) % 8)]
    csi_data = np.frombuffer(csi_binary, dtype=np.complex64).copy()
    num_sub_car = len(csi_data)
    num_sub_car_per_group = 2
    num_groups = num_sub_car // num_sub_car_per_group

    nan_or_inf = np.isnan(csi_data) | np.isinf(csi_data)
    csi_data[nan_or_inf] = 0
    frequency_domain_csi = np.array(csi_data)
    frequency_domain_csi /= np.max(csi_data)

    grouped_responses = [np.mean(frequency_domain_csi[i * num_sub_car_per_group: (i + 1) * num_sub_car_per_group]) for i in range(num_groups)]
    grouped_responses = np.array(grouped_responses)
    grouped_responses[np.isinf(grouped_responses)] = 0
    time_domain_csi = ifft(grouped_responses)
    time_domain_amplitude = -1 * np.log10(np.abs(time_domain_csi))
    filtering = truncation(time_domain_amplitude)

    for i in range(0, num_sub_car):
        arr_num_car.append(i)
    return arr_num_car, grouped_responses, time_domain_amplitude, filtering
