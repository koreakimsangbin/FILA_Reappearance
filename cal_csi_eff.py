import numpy as np


def calculate_CSIEff(num_carrier, frequencies, amplitudes, central_frequency):
    sum_values = 0
    for k in range(1, num_carrier):
        fk = frequencies[k]
        Ak = amplitudes[k]
        sum_values += (fk / central_frequency) * np.abs(Ak)

    CSIEff = sum_values / num_carrier
    return CSIEff
