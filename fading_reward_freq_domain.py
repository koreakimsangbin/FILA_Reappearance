import numpy as np


def fading_reward_freq_domain(csi_values, csieff):
    compensated_csi = csi_values * csieff

    return compensated_csi
