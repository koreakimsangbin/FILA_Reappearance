from matplotlib import pyplot as plt
from scipy.fft import ifft
from truncation_window import *
import math
def get_time_domain(file_path):
    with open(file_path, 'rb') as f:
        csi_binary = f.read()

    csi_data = np.frombuffer(csi_binary, dtype=np.complex128).copy()
    num_sub_car = len(csi_data)
    num_sub_car_per_group = 160
    num_groups = num_sub_car // num_sub_car_per_group
    nan_or_inf = np.isnan(csi_data) | np.isinf(csi_data)
    csi_data[nan_or_inf] = 0
    frequency_domain_csi = np.array(csi_data)
    frequency_domain_csi /= np.max(np.abs(csi_data))
    grouped_responses = [np.mean(frequency_domain_csi[i * num_sub_car_per_group: (i + 1) * num_sub_car_per_group]) for i in range(num_groups)]

    time_domain_csi = ifft(grouped_responses)
    time_domain_amplitude = np.abs(time_domain_csi[: num_groups])
    time_domain_amplitude_db = np.abs(10 * np.log10(time_domain_amplitude))
    filtering = truncation(time_domain_amplitude_db)

    return time_domain_amplitude_db, filtering
