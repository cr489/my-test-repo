import numpy as np

class stat:


    # eliminate columns based on the variance: if the variance of the values
    # in a column is below a given threshold, that column is discarded
    def exp_drop(file_ex, thr_val):
        """Function to drop columns with values below set threshold."""
        