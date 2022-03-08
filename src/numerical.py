import numpy as np


def num_crl(wf_n):
    """Function computes the autocorrelation function from given vectors\
    and the Discrete Fourier transform

    Args:
        wf_n(numpy array, complex): Wave function over time

    Returns:
        numpy array, complex: The wave function complex over time.
        numpy array, complex: The autocorrelation function over time.
        numpy array, complex: The Discrete Fourier Transformation function\
        over frequency
    """

    # setting up the time vector and deleting it from array
    time_vc = np.zeros([len(wf_n[0])])
    time_vc = wf_n[0]
    wf_n = np.delete(wf_n, [0], axis=0)

    # the lenth of the vector
    t_wf = len(wf_n[0])
    p_wf = len(wf_n[:, 0])

    # turning array into complex
    comp_vc = np.zeros([p_wf, t_wf], dtype=np.complex_)
    for n in range(p_wf):
        comp_vc[:, n] = wf_n[n * 2] + wf_n[1 + n * 2] * 1j
    return comp_vc, time_vc


def auto_corr(comp_vc, p_wf, t_wf):
    """Function computes the autocorrelation function from given vectors
    Args:
        wf_n(numpy array, complex): Wave function over time

    Returns:
        numpy array, complex: The autocorrelation function over time.
    """

    # autocorrelation fuction
    ac_file = np.zeros([p_wf, t_wf + 1], dtype=np.complex_)
    for n in range(p_wf):
        ac_file[n] = np.sum(comp_vc[:, 0] * np.conjugate(comp_vc[:, n]))
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
    FT_file = np.fft.fft(ac_file)
    FT_t = np.fft.fftfreq(len(ac_file))
    return FT_file, FT_t
