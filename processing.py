import warnings
from get_freq_domain import *
from get_time_domain import *
from fading_reward_freq_domain import *
from calibration_distance import *

def processing(file_path):
    wave_speed = 3 * (10 ** 8)
    time_domain_no_filtering, time_domain_filtering = get_time_domain(file_path)
    time_to_freq_domain, csi_eff, central_freq = get_freq_domain(time_domain_filtering)
    time_to_freq_domain_db = np.abs(10 * np.log10(np.abs(time_to_freq_domain)))
    freq_domain = fading_reward_freq_domain(time_to_freq_domain, csi_eff)
    freq_domain_db = np.abs(10 * np.log10(np.abs(freq_domain)))
    warnings.simplefilter("ignore", np.ComplexWarning)
    distance = calculate_distance(wave_speed, central_freq, csi_eff, 4, 3)
    plt.plot(time_domain_no_filtering, label='Before Filtering', color='red', linestyle='-')
    plt.plot(time_domain_filtering, label='After Filtering', color='blue', linestyle='--')
    plt.xlabel('Time or Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Time Domain Channel Response')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.plot(freq_domain_db, label='After reward', color='blue', linestyle='-')
    plt.plot(time_to_freq_domain_db, label='before reward', color='red', linestyle='--')
    plt.xlabel('Time or Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain')
    plt.grid(True)
    plt.legend()
    plt.show()
    distance = round(distance, 2)

    print("distance: ", distance)

    return distance