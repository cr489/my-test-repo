import numpy as np


def cmplx_array(file):
    """Function to create an array of complex dtype from numpy.float array\

    Args:
        wf_n(numpy array, float): Wave function over time

    Returns:
        numpy array, complex: The wave function complex over time.
        numpy array, float: The time column as an array.
    """

    # loading file as a numpy array dtype=float
    arr_fl = np.loadtxt("../data/nstate_i.t", dtype=float, skiprows=1)

    # storing time column as a vector and droping from arr_fl
    time = arr_fl[:, 0]
    arr_fl = np.delete(arr_fl, 0, axis=1)

    # creating numpy array with dtype=float from arr_fl
    r_arr = arr_fl[:, 0::2]
    im_arr = arr_fl[:, 1::2]
    arr_cmplx = 1j * im_arr
    arr_cmplx += r_arr

    return arr_cmplx, time


def auto_corr(arr_cmplx, time):
    """Function computes the autocorrelation function from given vectors
    Args:
        arr_cmplx(numpy array, complex): Wave function over time
        time(numpy array, float): time column

    Returns:
        numpy array, complex: The autocorrelation function over time.
    """
    t_len = len(time)
    # creating arrays
    init_wf = arr_cmplx[0, :]
    prop_wf = arr_cmplx[:, :]
    # autocorrelation fuction
    ac_file = np.zeros([t_len], dtype=np.complex)
    for i in range(t_len):
        ac_file[i] = np.correlate(init_wf, prop_wf[i, :])

    return ac_file


def FFT_wf(ac_file):
    """Function computes the autocorrelation function from given vectors
    and the Discrete Fourier transform

    Args:
        ac_file(numpy array, complex): Autocorrelation function form the\
        Wave function over time

    Returns:
        numpy array, complex: The Discrete Fourier Transformation function\
        over frequency
    """
    FT1_file = np.fft.fft(ac_file)
    FT1_t = np.fft.fftfreq(len(ac_file))

    FT_file = FT1_file[0 : len(ac_file) // 2]  # Dropping the negative part
    FT_t = FT1_t[0 : len(ac_file) // 2]  # Dropping the negative part

    return FT_file, FT_t
