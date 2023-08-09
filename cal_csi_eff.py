import numpy as np


def calculate_CSIEff(frequencies, amplitudes, central_frequency):
    sum_values = 0
    for k in range(1, len(frequencies)):
        fk = frequencies[k]
        Ak = amplitudes[k]
        sum_values += (fk / central_frequency) * Ak

    CSIEff = sum_values / len(frequencies)
    return CSIEff
