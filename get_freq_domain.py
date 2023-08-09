from find_csi_parameter import *
from scipy.fft import fft
from cal_csi_eff import *


def get_freq_domain(get_time_domain):
    time_to_freq = fft(get_time_domain)
    frequencies, amplitudes, central_frequency = extract_parameters(time_to_freq)
    csi_eff = calculate_CSIEff(frequencies, amplitudes, central_frequency)

    return time_to_freq, csi_eff, central_frequency
