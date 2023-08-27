import warnings

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from calibration_distance import calculate_distance
from get_freq_domain import get_freq_domain
from get_time_domain import get_time_domain

class DistanceEstimator:

    def __init__(self, delta=1.0, n=2.0):
        self.delta = delta
        self.n = n
        self.model = LinearRegression()

    def get_params(self, deep=True):
        # Return estimator parameter dictionary
        return {"delta": self.delta, "n": self.n}

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self

    def fit(self, X, y):
        y = calculate_distance(c=3e8, f0=24e8, CSIeff=X, sigma=self.delta, n=self.n)
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)

def main_training(file_list):
    initial_delta = 1
    initial_n = 2
    csi_eff_values = []
    distance_values = []
    for file_path in file_list:
        groups_num, first_freq_domain, time_domain_no_filtering, time_domain_filtering = get_time_domain(file_path)
        time_to_freq_domain, csi_eff, central_freq = get_freq_domain(time_domain_filtering)
        warnings.simplefilter("ignore", np.ComplexWarning)
        csi_eff_values.append(csi_eff)
        distance_values.append(calculate_distance(c=3e8, f0=2.45e9, CSIeff=csi_eff, sigma=initial_delta, n=initial_n))
    X = np.array(csi_eff_values).reshape(-1, 1)
    y = np.array(distance_values)

    param_grid = {
        'delta': np.arange(2, 5, 0.1),
        'n': np.arange(4, 5, 0.1)
    }

    estimator = DistanceEstimator()
    grid_search = GridSearchCV(estimator, param_grid, cv=416, scoring='neg_mean_squared_error')  # cv는 교차 검증 횟수입니다.

    grid_search.fit(X, y)

    best_params = grid_search.best_params_
    best_estimator = grid_search.best_estimator_
    print("Training complete with δ:", best_params['delta'], "and n:", best_params['n'])


    return best_params['delta'], best_params['n'], best_estimator