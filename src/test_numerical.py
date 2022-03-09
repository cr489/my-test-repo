import pytest
import numerical
import numpy as np

my_wf = "../data/nstate_i.t"


def test_num_crl():
    test1 = numerical.num_crl(my_wf)
    assert test1.dtype == np.complex_


def test_auto_corr():
    test2 = numerical.auto_corr()
