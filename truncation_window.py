import numpy as np


def truncation(csi_time_domain):
    time_domain_amp = np.array(np.abs(csi_time_domain))
    threshold = 0.5 * np.max(time_domain_amp)
    first_cluster_indices = np.where(time_domain_amp > threshold)[0]
    first_cluster_start = first_cluster_indices[0]
    first_cluster_end = first_cluster_indices[-1] + 1

    filtered_time_domain_amplitude = np.zeros_like(csi_time_domain)
    filtered_time_domain_amplitude[first_cluster_start:first_cluster_end] = csi_time_domain[first_cluster_start:first_cluster_end]

    return filtered_time_domain_amplitude