import numpy as np

def generate_signal(N=100, r_cp=0.66, amp_cp=3, trend=4, puls=24, sig_noise=1.):
    """Generate a time serie with change point, trend, seasonality, and noise
    Return the decomposition of the signal from raw to final, and a bool that indicate
    if there was a change point.

    Args:
        N: Length of the signal (default 100)
        r_cp: Proportion of signal before change point (default 0.66)
        amp_cp: Amplitude of the change point (default 3)
        trend: amplitude of the trend (default 4)
        puls: Pulsation for the seasonality (default 24)
        sig_noise: Standard deviation for the noise (default 1.)

    Returns:
        y0: the initial signal.
        y1: the initial signal + trend.
        y2: the initial signal + trend + seasonality.
        y3: the initial signal + trend + seasonality + noise
        there_is_cp: True if there is a change point in the signal

    """
    ### Initialize time and signal of length N.
    t = np.arange(N)
    y0 = np.zeros(N)
    ### Adding a change point (cp) if the change amplitude is different from 0.
    there_is_cp = amp_cp != 0
    if there_is_cp:
        t_cp = int(N * r_cp)
        y0[t_cp:] += amp_cp
    ### Adding trend if trend amplitude different from 0.
    if trend != 0:
        y1 = y0 + np.linspace(0, trend, N)
    else: y1 = y0
    ### Adding seasonality if pulsation is different from infinite.
    if puls != np.inf:
        y2 = y1 + np.sin(2 * np.pi * t / puls)
    else: y2 = y1
    ### Adding noise if std of noise different from 0.
    if sig_noise != 0:
        y3 = y2 + np.random.normal(loc=0, scale=sig_noise, size=N)
    else: y3 = y2
    return y0, y1, y2, y3, there_is_cp 
