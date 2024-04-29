import importlib
import itertools
from string import ascii_uppercase

import numpy as np
from scipy.stats import median_abs_deviation


def is_gpu():
    return importlib.util.find_spec('cupy') != None


def round_nearest(x, a):
    return round(x / a) * a


def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False


def tqdm_importer():
    if is_notebook:
        pass
    else:
        pass


def demad(x, factor=10.0):
    """Normalize signal with median absolute deviation.

    Parameters
    ----------
    x : np.ndarray
        The input signal.
    factor : float, optional
        An additional normalization factor.

    Returns
    -------
    The data normalized with median absolute deviation.
    """
    mad = median_abs_deviation(x)
    return x / np.mean(mad) / factor


COLORS = [
    '0.8',
    '#222222',
    '#F3C300',
    '#875692',
    '#F38400',
    '#A1CAF1',
    '#BE0032',
    '#C2B280',
    '#848482',
    '#008856',
    '#E68FAC',
    '#0067A5',
    '#F99379',
    '#604E97',
    '#F6A600',
    '#B3446C',
    '#DCD300',
    '#882D17',
    '#8DB600',
    '#654522',
    '#E25822',
    '#2B3D26',
    '0.8',
    '#222222',
    '#F3C300',
    '#875692',
    '#F38400',
    '#A1CAF1',
    '#BE0032',
    '#C2B280',
    '#848482',
    '#008856',
    '#E68FAC',
    '#0067A5',
    '#F99379',
    '#604E97',
    '#F6A600',
    '#B3446C',
    '#DCD300',
    '#882D17',
    '#8DB600',
    '#654522',
    '#E25822',
    '#2B3D26',
    '0.8',
    '#222222',
    '#F3C300',
    '#875692',
    '#F38400',
    '#A1CAF1',
    '#BE0032',
    '#C2B280',
    '#848482',
    '#008856',
    '#E68FAC',
    '#0067A5',
    '#F99379',
    '#604E97',
    '#F6A600',
    '#B3446C',
    '#DCD300',
    '#882D17',
    '#8DB600',
    '#654522',
    '#E25822',
    '#2B3D26',
]


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield ''.join(s)


def list_of_strings(number_letters):
    return [s for s in itertools.islice(iter_all_strings(), number_letters)]
