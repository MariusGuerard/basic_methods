# Basic Signal Processing Methods

These notebooks are gathering few technics for processing time-serie like signals.

- signal_simulation.ipynb is describing the different components that we add to create our simulated signal (trend, seasonality, change point, noise, ...).

- helper_signal.py implements the notebook just described in a function that can be used in other notebook (as signal_smoothing.ipynb).

- signal_smoothing.ipynb is presenting different methods to denoise a signal.

- testing_normality.ipynb is presenting different methods and statistical tests to assess if a sample is drawn from a unimodal, normal distribution.

- compressing_time_serie_model.ipynb is giving an exemple of frequential decoding of a time serie. From one time serie, we retrieve different features encoded at different frequencies.