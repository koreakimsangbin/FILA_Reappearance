import numpy as np


def truncation(csi_time_domain):
    max_peak = np.max(csi_time_domain)
    threshold = 0.5 * max_peak
    first_cluster_indices = np.where(csi_time_domain > threshold)[0]
    first_cluster_start = first_cluster_indices[0]

    filtered_time_domain_amplitude = np.zeros_like(csi_time_domain)
    for i in range(first_cluster_start, len(first_cluster_indices)):
        filtered_time_domain_amplitude[first_cluster_indices[i]] = csi_time_domain[first_cluster_indices[i]]

    return filtered_time_domain_amplitude
