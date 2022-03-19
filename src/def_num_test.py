import unittest
import numerical as nm


class test_cmplx_array(unittest.TestCase):
    nstate = "../data/nstate_i.t"

    # out_file is a dictionary containing the complex array and time array
    out_file = nm.cmplx_array(nstate)
    arr_cmplx = out_file["arr_cmplx"]
    t = out_file["time"]

    def test_cmplx_array(self):
        """Test the output of cmplx_array is a complex array"""
        self.assertEqual(self.arr_cmplx.dtype, complex)

    def test_dtype(self):
        """Make sure the dtype errors are recognised for cmplx_array"""

        self.assertRaises(ValueError, nm.cmplx_array, -1)


# class test_auto_corr(unittest.TestCase):
#    nstate = "../data/nstate_i.t"
#    cmplx_out = nm.cmplx_array(nstate)
#
#    def test_auto_corr(self):
#        """Test the autocorrelation function values for a given wave\
#            function (complex numpy array of vectors at different times)
#        """
#
#        auto_arr = nm.auto_corr(self.cmplx_file)
#
#        for i in range(len(auto_arr)):
#            self.assertLessEqual(auto_arr[i], 1)
#
#    def test_values(self):
#        """Make sure value errors are recognised for auto_corr"""
#
#        self.assertRaises(ValueError, nm.auto_corr(self.cmplx_file), -5)
