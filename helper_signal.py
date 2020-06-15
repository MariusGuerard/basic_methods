import numpy as np
import random

def generate_signal(signal_l=100, r_cp=0.66, amp_cp=3, trend=4, A_season = 10,
                    puls=24, A_noise=1., detail_output=True):
    """Generate a time serie with change point, trend, seasonality, and noise
    Return the decomposition of the signal from raw to final, and a bool that indicate
    if there was a change point.

    Args:
        signal_l: Length of the signal (default 100)
        r_cp: Proportion of signal before change point (default 0.66)
        amp_cp: Amplitude of the change point (default 3)
        trend: amplitude of the trend (default 4)
        puls: Pulsation for the seasonality (default 24)
        A_noise: Standard deviation for the noise (default 1.)

    Returns:
        y0: the initial signal.
        y1: the initial signal + trend.
        y2: the initial signal + trend + seasonality.
        y3: the initial signal + trend + seasonality + noise
        there_is_cp: True if there is a change point in the signal

    """
    ### Initialize time and signal of length signal_l.
    t = np.arange(signal_l)
    y0 = np.zeros(signal_l)
    ### Adding a change point (cp) if the change amplitude is different from 0.
    there_is_cp = amp_cp != 0
    if there_is_cp:
        t_cp = int(signal_l * r_cp)
        y0[:t_cp] -= amp_cp
        y0[t_cp:] += amp_cp 
        
    ### Adding trend if trend amplitude different from 0.
    if trend != 0:
        y1 = y0 + np.linspace(0, trend, signal_l)
    else: y1 = y0
    ### Adding seasonality if pulsation is different from infinite.
    if puls != np.inf:
        y2 = y1 + A_season * np.sin(2 * np.pi * t / puls)
    else: y2 = y1
    ### Adding noise if std of noise different from 0.
    if A_noise != 0:
        y3 = y2 + np.random.normal(loc=0, scale=A_noise, size=signal_l)
    else: y3 = y2
    ### Returning different detail of output (just raw or decomposition).
    if detail_output:
        return y0, y1, y2, y3, there_is_cp 
    else:
        return y3


def flip(proba=0.5):
    """Return 1 with probability 'proba', 0 otherwise
    (biaised coin if proba != 0.5)
    """
    return random.random() < proba
    
    
def generate_dataset(n=1000, signal_l=100, p_changepoint=0.5, amp_change=3):
    """Simulate time_series (X) and labels (y = 1 if change point)
    to compare different change point methods
    """
    X = np.zeros((n, signal_l))
    y = np.zeros(n)

    for row in range(n):
        there_is_cp = flip(p_changepoint)
        amp_tmp = amp_change * there_is_cp 
        raw_signal = generate_signal(signal_l=signal_l, amp_cp=amp_tmp,
                                     detail_output=False)
        X[row] = raw_signal
        y[row] = there_is_cp
    return X, y
