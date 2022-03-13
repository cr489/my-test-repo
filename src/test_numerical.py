import pytest
import numerical
import numpy as np

my_wf = np.loadtxt('../data/nstate_i.t', dtype=float, skiprows=1)

def test_cmplx_array():
    test1 = numerical.cmplx_array(my_wf)
    assert test1[0].dtype == np.complex_

#def test_auto_corr():
#    test2 = numerical.auto_corr() 