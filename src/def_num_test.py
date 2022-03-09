import unittest

# import numpy as np
import numerical as num


class test_auto_corr(unittest.TestCase):
    def test_auto_corr(self):
        """Test the autocorrelation function values for a given wave\
            function (complex numpy array of vectors at different times)
        """
        auto_arr = num.auto_corr()  # need insert something in () ??
        for i in range(len(auto_arr)):

            self.assertLessEqual(auto_arr[i], 1)

    def test_values(self):
        """MAke sure value errors are recognised for auto_corr"""

        self.assertRaises(ValueError, num.auto_corr, -5)
