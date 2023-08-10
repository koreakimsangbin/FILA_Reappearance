import math

import numpy as np
from sympy import symbols, Eq, solve

def cal_coordinate(A, B, C, d_a, d_b, d_c):
    m_x = ((d_a ** 2) - (d_b ** 2) + (B[0] ** 2)) / (2 * B[0])
    m_y = ((C[0] ** 2) + (C[1] ** 2) + (d_a ** 2) - (d_c ** 2) - 2 * m_x * C[0]) / (2 * C[1])
    m_z = math.sqrt(np.abs((d_a ** 2) - (m_x ** 2) - (m_y ** 2)))

    return m_x, m_y, m_z

