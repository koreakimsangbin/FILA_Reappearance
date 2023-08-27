import os
import warnings
from get_freq_domain import *
from get_time_domain import *
from fading_reward_freq_domain import *
from calibration_distance import *
from make_list import make_list
from train import *

def processing(file_path, delta, n):
    wave_speed = 3 * (10 ** 8)
    groups_num, first_freq_domain, time_domain_no_filtering, time_domain_filtering = get_time_domain(file_path)
    time_to_freq_domain, csi_eff, central_freq = get_freq_domain(time_domain_filtering)
    warnings.simplefilter("ignore", np.ComplexWarning)



    distance = np.abs(np.log10(calculate_distance(wave_speed, central_freq, csi_eff, delta, n)))
    """
    plt.plot(first_freq_domain)
    plt.xlabel('Time or Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain')
    plt.grid(True)
    plt.show()

    plt.plot(time_domain_no_filtering, label='Before Filtering', color='red', linestyle='-')
    plt.plot(time_domain_filtering, label='After Filtering', color='blue', linestyle='--')
    plt.xlabel('Time or Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Time Domain Channel Response')
    plt.grid(True)
    plt.show()

    #plt.plot(first_freq_domain, color='blue', linestyle='-.')
    plt.plot(time_to_freq_domain, label='after reward', color='red', linestyle='--')
    plt.xlabel('Time or Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain')
    plt.grid(True)
    plt.show()
    distance = round(distance, 2)
    """

    print("distance: ", distance)

    return distance * 20, csi_eff