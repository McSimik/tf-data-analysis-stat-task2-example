import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 964993301 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = (1-p)/2
    beta=1-alpha
    loc = (x.mean()+1/2)/4802
    return loc +1/2 - expon.ppf(beta) \
           loc +1/2 - expon.ppf(alpha)
