import pytest
import numerical
import numpy as np

my_wf = np.loadtxt('../data/nstate_i.t', dtype=float, skiprows=1)

@pytest.mark.test1
def test_cmplx_array():
    test1 = numerical.cmplx_array(my_wf)
    #cmplx_array returns tuple, accessing arr_cmplx
    assert test1[0].dtype == np.complex_

@pytest.mark.test2
def test_auto_corr():
    #getting tuple from cmplx_array function
    wf_tuple = numerical.cmplx_array(my_wf)
    test2 = numerical.auto_corr(wf_tuple[0], wf_tuple[1])
    assert test2[0] == np.complex_ #is being complex enough?

@pytest.mark.test3
def test_FFT_wf():
    wf_tuple = numerical.cmplx_array(my_wf)
    test3 = numerical.FFT_wf(wf_tuple)
    assert test3 == np.complex_