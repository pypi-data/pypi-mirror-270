import typing as _t

import numpy as np

from ..fit_logic import FitLogic
from ..utils import _NDARRAY, check_min_len


class CosParam(_t.NamedTuple):
    amplitude: float
    frequency: float
    phi0: float
    offset: float


def normalize_res_list(x: _t.Sequence[float]) -> list:
    return [
        abs(x[0]),
        x[1],
        (x[2] + (np.pi if x[0] < 0 else 0)) % (2 * np.pi),
        x[3],
    ]


def cos_func(x: _NDARRAY, amplitude: float, frequency: float, phi0: float, offset: float):
    return amplitude * np.cos(2 * np.pi * x * frequency + phi0) + offset


def cos_guess(x: _NDARRAY, y: _NDARRAY, **kwargs):
    """Guess the initial parameters for fitting a curve to the given data.

    Parameters:
    - x: array-like
        The x-coordinates of the data points.
    - y: array-like
        The y-coordinates of the data points.
    - **kwargs: keyword arguments
        Additional arguments that can be passed to the function.

    Returns:
    - list
        A list containing the initial parameter guesses for fitting the curve.
        The list contains the following elements:
        - sign_ * amp_guess: float
            The amplitude guess for the curve.
        - period: float
            The period guess for the curve.
        - off_guess: float
            The offset guess for the curve.
    """
    del kwargs
    if not check_min_len(x, y, 3):
        return np.zeros(4)

    off_guess: float = np.mean(y)  # type: ignore
    amp_guess: float = np.abs(np.max(y - off_guess))
    nnn = 10 * len(y)
    fft_vals = np.fft.rfft(y - off_guess, n=nnn)
    fft_freqs = np.fft.rfftfreq(nnn, d=x[1] - x[0])
    freq_max_index = np.argmax(np.abs(fft_vals))
    freq_guess: float = np.abs(fft_freqs[freq_max_index])
    sign_: float = np.sign(np.real(fft_vals[freq_max_index]))  # type: ignore
    phase: float = np.imag(fft_vals[freq_max_index])

    return np.array(normalize_res_list([sign_ * amp_guess, freq_guess, phase, off_guess]))


class Cos(FitLogic[CosParam]):
    r"""Fit Cos function.


    Function
    ---------

    $$
    f(x) = A * cos(2 * pi * \omega* x + \phi_0) + A_0
    $$

        f(x) = amplitude * cos(2 * pi * frequency * x + phi0) + offset

    Example
    ---------
        >>> import ffit as ff
        >>> res = ff.Cos.fit(x, y).res

        >>> res = ff.Cos.fit(x, y, guess=[1, 2, 3, 4]).plot(ax).res
        >>> amplitude = res.amplitude

    Final parameters
    -----------------
    - `amplitude`: float.
        The amplitude.
    - `frequency`: float.
        The frequency in 1/[x] units.
    - `phi0`: float.
        The phase inside cos.
    - `offset`: float.
        The global offset.

    """

    param: _t.Type[CosParam] = CosParam
    func = cos_func
    normalize_res = normalize_res_list
    _guess = cos_guess
